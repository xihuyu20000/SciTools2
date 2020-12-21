<template>
  <vxe-modal v-model="drawerVisible" width="800" height="80%" min-width="400" min-height="320" :mask="true" :mask-closable="true" :esc-closable="true" show-zoom resize remember storage transfer>
    <template v-slot:title>
      <span style="color: red;">数据清洗引擎</span>
    </template>
    <template v-slot>
      <el-card class="box-card">
        <el-button type="primary" plain v-for="(field, i) in fieldArray" :key="i" @click="clickFieldBtn(field)">{{ field.title }}</el-button>
      </el-card>
      <vxe-list height="100%" :data="expressArray" :scroll-y="{ gt: 60, sItem: '.my-tr' }">
        <template v-slot="{ items }">
          <table>
            <thead>
              <tr>
                <th style="width:150px;text-align:center;">字段</th>
                <th style="width:100px;text-align:center;">函数</th>
                <th style="width:100px;text-align:center;">参数1</th>
                <th style="width:100px;text-align:center;">参数2</th>
                <th style="width:100px;text-align:center;">新列</th>
                <th style="width:150px;text-align:center;">操作</th>
              </tr>
            </thead>
            <tbody>
              <tr :field="field" v-for="(field, i) in items" :key="i">
                <td style="max-width:150px;">{{ field.title }}</td>
                <td style="width:100px;">
                  <el-select v-model="expressArray[i].func" placeholder="请点击" style="width:100px;margin:0 10px;" @change="changeFunc">
                    <el-option v-for="(func, j) in field.funcs" :label="func.label" :value="func.name" :key="j"></el-option>
                  </el-select>
                </td>
                <td style="width:100px"><el-input v-model="expressArray[i].param1" :disabled="true" style="width:100px"></el-input></td>
                <td style="width:100px"><el-input v-model="expressArray[i].param2" :disabled="true" style="width:100px"></el-input></td>
                <td><vxe-switch v-model="expressArray[i].newcol" open-label="是" close-label="否"></vxe-switch></td>
                <td style="width:150px;">
                  <i class="el-icon-thumb" style="color:blue;"></i>
                  <i class="el-icon-refresh-left"></i>
                  <i class="el-icon-bottom"></i>
                  <i class="el-icon-top"></i>
                  <i class="el-icon-delete"></i>
                </td>
              </tr>
            </tbody>
          </table>
        </template>
      </vxe-list>
    </template>
  </vxe-modal>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      drawerVisible: false,
      ad_tbl: {},
      fieldArray: [],
      expressArray: [],
      text_funcs: [
        { label: '删除行', name: 'delete_rows', param1: true, param2: false, desc: '删除行，填写行号' },
        { label: '删除列', name: 'delete_cols', param1: true, param2: false, desc: '删除列，填写列名' },
        { label: '删除空白', name: 'delete_null', param1: false, param2: false, desc: '判断是否没有内容的行' },
        { label: '填充空白', name: 'fill_null', param1: true, param2: false, desc: '填充没有内容的单元格，第1个参数是填充值' },
        { label: '包含', name: 'include', param1: true, param2: false, desc: '判断是否特定内容' },
        { label: '分割', name: 'split', param1: true, param2: false, desc: '分割文本，填写分隔符' },
        { label: '合并', name: 'join', param1: true, param2: false, desc: '合并列，填写列名' },
        { label: '替换', name: 'replace', param1: true, param2: true, desc: '替换文本，第1个参数是原文本，第2个参数是新文本' },
        { label: '分词', name: 'cutwords', param1: false, param2: false, desc: '对文本分词，停用词和自定义词，可以配置' }
      ],
      number_funcs: [
        { label: '删除行', name: 'delete_rows', param1: true, param2: false, desc: '删除行，填写行号' },
        { label: '删除列', name: 'delete_cols', param1: true, param2: false, desc: '删除列，填写列名' },
        { label: '删除空白', name: 'delete_null', param1: false, param2: false, desc: '判断是否没有内容的行' },
        { label: '填充空白', name: 'fill_null', param1: true, param2: false, desc: '填充没有内容的单元格，第1个参数是填充值' },
        { label: '大于', name: 'gt', param1: true, param2: false, desc: '大于某个数' },
        { label: '等于', name: 'eq', param1: true, param2: false, desc: '等于某个数' }
      ],
      date_funcs: [
        { label: '删除行', name: 'delete_rows', param1: true, param2: false, desc: '删除行，填写行号' },
        { label: '删除列', name: 'delete_cols', param1: true, param2: false, desc: '删除列，填写列名' },
        { label: '删除空白', name: 'delete_null', param1: false, param2: false, desc: '判断是否没有内容的行' },
        { label: '填充空白', name: 'fill_null', param1: true, param2: false, desc: '填充没有内容的单元格，第1个参数是填充值' },
        { label: '转格式', name: 'format_date', param1: true, param2: false, desc: '转换日期函数，第1个参数是格式文本' }
      ]
    }
  },
  watch: {},
  methods: {
    async fetch() {
      const { data: resp } = await this.$http.get(this.$api.advanced_tbls_list_fieldconfigs + '/' + this.ad_tbl.tblid)
      if (resp.status == 400) return this.$message.error(resp.msg)
      this.fieldArray = resp.data
      // 根据字段的类型，添加函数
      this.fieldArray = this.fieldArray.map(field => {
        if (field.style == '文本') {
          field.funcs = this.text_funcs
        }
        if (field.style == '数值') {
          field.funcs = this.number_funcs
        }
        if (field.style == '日期') {
          field.funcs = this.date_funcs
        }
        return field
      })
    },
    clickFieldBtn(field) {
      this.expressArray.push(field)
    },
    changeFunc(v) {
      console.log('函数', v)
    }
  },
  mounted() {
    this.$bus.$on('show_cleaning_data_filter', ad_tbl => {
      this.ad_tbl = ad_tbl
      this.drawerVisible = true
      this.fetch()
    })
  }
}
</script>

<style lang="scss" scoped>
.el-drawer__body {
  height: 0;
  overflow: scroll;
}
</style>
