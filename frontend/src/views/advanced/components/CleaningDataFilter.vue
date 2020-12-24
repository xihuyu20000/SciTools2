<template>
  <vxe-modal v-model="drawerVisible" width="760" height="80%" min-width="400" min-height="320" :mask="true" :mask-closable="true" :esc-closable="true" show-zoom resize remember storage transfer>
    <template v-slot:title>
      <span style="color: red;">数据清洗引擎</span>
    </template>
    <template v-slot>
      <el-card style="display:flex; justify-content: flex-start">
        <el-button type="primary" plain v-for="(field, i) in fieldArray" :key="i" @click="clickFieldBtn(field)" style="margin-bottom:10px">{{ field.title }}</el-button>
      </el-card>
      <el-table :data="expressArray" size="small" style="margin-top:10px;width: 100%">
        <el-table-column label="字段" prop="field.title" width="100" />
        <el-table-column label="函数" width="150">
          <template slot-scope="scope">
            <el-select v-model="scope.row.func" placeholder="请点击" width="100" @change="selectFunc($event, scope)">
              <el-option v-for="(func, j) in scope.row.field.funcs" :label="func.label" :value="func.name" :key="j"></el-option>
            </el-select>
          </template>
        </el-table-column>
        <el-table-column label="参数1" width="100">
          <template slot-scope="scope">
            <el-input v-model="scope.row.param1" :disabled="!scope.row.p1editable" width="100"></el-input>
          </template>
        </el-table-column>
        <el-table-column label="参数2" width="100">
          <template slot-scope="scope">
            <el-input v-model="scope.row.param2" :disabled="!scope.row.p2editable" width="100"></el-input>
          </template>
        </el-table-column>
        <el-table-column label="新列" width="100">
          <template slot-scope="scope"><vxe-switch v-model="scope.row.newcol" :disabled="!scope.row.neweditable" open-label="是" close-label="否"></vxe-switch> </template
        ></el-table-column>
        <el-table-column label="操作" width="180">
          <template slot-scope="scope">
            <el-button icon="el-icon-thumb" style="color:blue;" @click="runExpress(scope.row)"></el-button>
            <el-button icon="el-icon-delete" @click="deleteExpress(scope.$index)"></el-button>
            <el-dropdown @command="chooseCommand" style="margin-left:10px">
              <span class="el-dropdown-link">更多</span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item icon="el-icon-top" :command="beforeChooseCommand(scope.$index, 'up')">上移</el-dropdown-item>
                <el-dropdown-item icon="el-icon-bottom" :command="beforeChooseCommand(scope.$index, 'down')">下移</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </template>
        </el-table-column>
      </el-table>
      <el-card style="display:flex; justify-content: space-around">
        <el-button type="info" @click="rollbackDataset">还原数据</el-button>
        <el-button type="primary" @click="batchRunCommand">批量执行</el-button>
        <el-button type="warning" @click="saveNewDataset">保存变化</el-button>
        <el-button type="danger" @click="saveAsNewDataset">另存为</el-button>
      </el-card>
    </template>
  </vxe-modal>
</template>

<script>
export default {
  props: ['titles', 'dataset'],
  components: {},
  data() {
    return {
      drawerVisible: false,
      ad_tbl: {},
      fieldArray: [],
      expressArray: [],
      common_funcs: [
        { label: '删除当前列', name: 'delete_cols', p1editable: false, p2editable: false, neweditable: false, desc: '删除当前列' },
        { label: '删除空白行', name: 'delete_null', p1editable: false, p2editable: false, neweditable: false, desc: '判断是否没有内容的行' },
        { label: '填充空白', name: 'fill_null', p1editable: true, p2editable: false, neweditable: false, desc: '填充没有内容的单元格，第1个参数是填充值' }
      ],
      text_funcs: [
        { label: '包含', name: 'text_include', p1editable: true, p2editable: false, neweditable: false, desc: '判断是否特定内容' },
        { label: '合并', name: 'text_join', p1editable: true, p2editable: true, neweditable: true, desc: '合并列，第1个参数是列名,多列名之间使用空格，第2个参数是连接符' },
        { label: '替换', name: 'text_replace', p1editable: true, p2editable: true, neweditable: false, desc: '替换文本，第1个参数是原文本，第2个参数是新文本' }
      ],
      number_funcs: [
        { label: '等于', name: 'number_eq', p1editable: true, p2editable: false, neweditable: false, desc: '等于某个数' },
        { label: '大于', name: 'number_gt', p1editable: true, p2editable: false, neweditable: false, desc: '大于某个数' },
        { label: '大于等于', name: 'number_gte', p1editable: true, p2editable: false, neweditable: false, desc: '大于等于某个数' },
        { label: '小于', name: 'number_lt', p1editable: true, p2editable: false, neweditable: false, desc: '小于某个数' },
        { label: '小于等于', name: 'number_lte', p1editable: true, p2editable: false, neweditable: false, desc: '小于等于某个数' }
      ],
      date_funcs: [{ label: '提取年', name: 'date_year', p1editable: false, p2editable: false, neweditable: false, desc: '提取年份函数' }]
    }
  },
  watch: {},
  mounted() {
    this.$bus.$on('show_cleaning_data_filter', ad_tbl => {
      this.ad_tbl = ad_tbl
      this.drawerVisible = true
      this.fetch()
    })
  },
  methods: {
    async fetch() {
      const { data: resp } = await this.$http.get(this.$api.advanced_tbls_list_fieldconfigs + '/' + this.ad_tbl.tblid)
      if (resp.status == 400) return this.$message.error(resp.msg)
      this.fieldArray = resp.data
      // 根据字段的类型，添加函数
      this.fieldArray = this.fieldArray.map(field => {
        if (field.style == '文本') {
          field.funcs = this.common_funcs.concat(this.text_funcs)
        }
        if (field.style == '数值') {
          field.funcs = this.common_funcs.concat(this.number_funcs)
        }
        if (field.style == '日期') {
          field.funcs = this.common_funcs.concat(this.date_funcs)
        }
        return field
      })
    },
    clickFieldBtn(field) {
      // 表达式默认结构
      let express_obj = { field: field, func: '', param1: '', param2: '', newcol: false, p1editable: false, p2editable: false, neweditable: false }
      this.expressArray.push(express_obj)
    },
    selectFunc(item, scope) {
      // 下拉框，选择某个函数
      console.log('下拉框选择某个函数', item, scope.$index)
      this.expressArray[scope.$index].field.funcs.forEach(func => {
        if (func.name == item) {
          this.expressArray[scope.$index].func = func.name
          this.expressArray[scope.$index].p1editable = func.p1editable
          this.expressArray[scope.$index].p2editable = func.p2editable
          this.expressArray[scope.$index].neweditable = func.neweditable
        }
      })
    },
    beforeChooseCommand(i, cmd) {
      return { index: i, cmd: cmd }
    },
    runExpress(express) {
      // 运行表达式
      console.log('运行表达式', express)
      let colname = express.field.field
      let func = express.func
      let param1 = express.param1
      let param2 = express.param2
      let newcol = express.newcol
      console.log('当前操作', colname, func, param1, param2, newcol)
      if (func == 'delete_cols') {
        let pos = this.titles.findIndex(x => x.field === colname)
        if (pos > 1) this.titles.splice(pos, 1)
      }
      if (func == 'delete_null') {
        for (let i = this.dataset.length - 1; i >= 0; i--) {
          if ((this.dataset[i][colname].length == 0) | ((this.dataset[i][colname].length == 1) & (this.dataset[i][colname][0] == ''))) {
            this.dataset.splice(i, 1)
          }
        }
      }
      if (func == 'fill_null') {
        for (let i = this.dataset.length - 1; i >= 0; i--) {
          if ((this.dataset[i][colname].length == 0) | ((this.dataset[i][colname].length == 1) & (this.dataset[i][colname][0] == ''))) {
            this.dataset[i][colname] = param1
          }
        }
      }
      if (func == 'text_include') {
        for (let i = this.dataset.length - 1; i >= 0; i--) {
          if (this.dataset[i][colname].search(param1) == -1) {
            this.dataset.splice(i, 1)
          }
        }
      }
      if (func == 'text_join') {
        let cols = param1.trim().split(/\s+/) // 这是显示名
        cols = cols.map(x => {
          let arr = this.titles.filter(y => y.title == x)
          return arr[0].field
        })

        if (!newcol) {
          this.dataset.forEach(row => {
            let v = Array()
            for (let n of cols) {
              v.push(row[n])
            }
            row[cols[0]] = v.join(param2)
          })
          return
        }
        // 产生新列
        let last_colname = this.titles[this.titles.length - 1].field
        last_colname = parseInt(last_colname.substr(1)) + 1
        let new_field = 'c' + last_colname // 新列名
        console.log('最后一列', new_field)
        this.titles.push({ field: new_field, resizable: true, sortable: true, style: '文本', title: '新列' + last_colname, width: '200px' })
        this.dataset.forEach(row => {
          let v = Array()
          for (let n of cols) {
            v.push(row[n])
          }

          row[new_field] = v.join(param2)
        })
      }
      if (func == 'text_replace') {
        this.dataset.forEach(row => {
          if (row[colname]) {
            row[colname] = row[colname].replace(new RegExp(param1, 'g'), param2)
          }
        })
      }
      if (func == 'number_eq') {
        for (let i = this.dataset.length - 1; i >= 0; i--) {
          if (parseInt(this.dataset[i][colname]) != parseInt(param1)) {
            this.dataset.splice(i, 1)
          }
        }
      }
      if (func == 'number_gt') {
        for (let i = this.dataset.length - 1; i >= 0; i--) {
          if (parseInt(this.dataset[i][colname]) <= parseInt(param1)) {
            this.dataset.splice(i, 1)
          }
        }
      }
      if (func == 'number_gte') {
        for (let i = this.dataset.length - 1; i >= 0; i--) {
          if (parseInt(this.dataset[i][colname]) < parseInt(param1)) {
            this.dataset.splice(i, 1)
          }
        }
      }
      if (func == 'number_lt') {
        for (let i = this.dataset.length - 1; i >= 0; i--) {
          if (parseInt(this.dataset[i][colname]) >= parseInt(param1)) {
            this.dataset.splice(i, 1)
          }
        }
      }
      if (func == 'number_lte') {
        for (let i = this.dataset.length - 1; i >= 0; i--) {
          if (parseInt(this.dataset[i][colname]) > parseInt(param1)) {
            this.dataset.splice(i, 1)
          }
        }
      }
      if (func == 'date_year') {
        this.dataset.forEach(row => {
          if (row[colname]) {
            row[colname] = row[colname].trim().slice(0, 4)
          }
        })
      }
    },
    deleteExpress(i) {
      // 删除表达式
      this.expressArray.splice(i, 1)
    },
    chooseCommand(obj) {
      // console.log('下拉菜单命令', obj)
      let i = obj.index
      if (obj.cmd == 'up') {
        // 上移
        if (i == 0) return
        // 在上一项插入该项
        this.expressArray.splice(obj.index - 1, 0, this.expressArray[obj.index])
        // 删除后一项
        this.expressArray.splice(obj.index + 1, 1)
      }
      if (obj.cmd == 'down') {
        // 下移
        if (i == this.expressArray.length - 1) return
        // 在下一项插入该项
        this.expressArray.splice(obj.index + 2, 0, this.expressArray[obj.index])
        // 删除前一项
        this.expressArray.splice(obj.index, 1)
      }
    },
    rollbackDataset() {
      // 还原数据集
      this.$bus.$emit('advanced_reload_dataset')
    },
    batchRunCommand() {
      // 批量执行命令
      this.expressArray.forEach(express => this.runExpress(express))
    },
    saveNewDataset() {
      // 保存变化后的数据
      this.$confirm('此操作永久性修改以前的数据, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(async () => {
        let titles2 = this.titles
          .filter((x, i) => i > 1)
          .map(x => {
            x.width = x.width.replace(new RegExp('px', 'g'), '')
            return x
          })
        // console.log('表头', titles2, this.dataset)
        let _url = this.$api.advanced_dataset_update
        const { data: resp } = await this.$http.post(_url, { tblid: this.ad_tbl.tblid, titles: titles2, dataset: this.dataset })
        if (resp.status == 400) return this.$message.error(resp.msg)
        this.$bus.$emit('advanced_reload_dataset')
        this.$bus.$emit('advanced_reload_adtbl_names')
        this.drawerVisible = false
      })
    },
    saveAsNewDataset() {
      // 保存变化后的数据
      this.$confirm('此操作会产生一个新的数据集，不会影响当前的数据, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(async () => {
        let titles2 = this.titles
          .filter((x, i) => i > 1)
          .map(x => {
            x.width = x.width.replace(new RegExp('px', 'g'), '')
            return x
          })
        let _url = this.$api.advanced_dataset_saveAsNew
        const { data: resp } = await this.$http.post(_url, { tblid: this.ad_tbl.tblid, titles: titles2, dataset: this.dataset })
        if (resp.status == 400) return this.$message.error(resp.msg)
        this.$bus.$emit('advanced_reload_adtbl_names')
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.c.el-table .cell {
  padding: 0;
}
</style>
