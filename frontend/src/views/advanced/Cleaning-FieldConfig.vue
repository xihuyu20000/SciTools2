<template>
  <!-- http://www.itxst.com/vue-draggable/tutorial.html -->
  <div class="main">
    <el-form :inline="true">
      <el-row :gutter="20" style="margin-top:50px">
        <el-col :offset="3" :span="18">
          <!--使用draggable组件-->
          <draggable v-model="dataArray" chosenClass="chosen" forceFallback="true" animation="200" @start="onStart" @end="onEnd">
            <transition-group>
              <div class="item" v-for="(element, i) in dataArray" :key="element.field">
                <el-form-item label="列名称" size="small"> <el-input v-model="dataArray[i].title" placeholder="列名称"> </el-input></el-form-item>
                <el-form-item label="列类型" size="small">
                  <el-select v-model="dataArray[i].style" placeholder="列类型">
                    <el-option label="文本" value="文本"></el-option>
                    <el-option label="数值" value="数值"></el-option>
                    <el-option label="日期" value="日期"></el-option>
                  </el-select>
                </el-form-item>
                <el-form-item label="列宽度" size="small"> <el-input v-model="dataArray[i].width" placeholder="列宽"> </el-input></el-form-item>
                <i class="el-icon-delete" @click="deleteItem(element.field)"></i>
              </div>
            </transition-group>
          </draggable>
        </el-col>
        <el-col :offset="11" :span="2">
          <el-button type="primary" @click="saveFieldConfig">保存配置</el-button>
        </el-col>
      </el-row>
    </el-form>
  </div>
</template>
<style scoped>
.main {
  width: 100%;
  height: 100vh;
}
/*被拖拽对象的样式*/
.item {
  padding: 10px 20px;
  background-color: #fdfdfd;
  border: solid 1px #eee;
  margin-bottom: 10px;
  cursor: move;
  display: flex;
  justify-content: space-around;
}
/*选中样式*/
.chosen {
  border: solid 2px #3089dc !important;
}
</style>
<script>
//导入draggable组件
import draggable from 'vuedraggable'
export default {
  //注册draggable组件
  components: {
    draggable
  },
  data() {
    return {
      tblid: '',
      dataArray: []
    }
  },
  created() {
    this.fetch()
  },
  methods: {
    async fetch() {
      this.tblid = this.$route.params.tblid
      const { data: resp } = await this.$http.get(this.$api.advanced_tbls_list_fieldconfigs + '/' + this.tblid)
      if (resp.status == 400) return this.$message.error(resp.msg)
      // console.log('标题配置信息', resp)
      this.dataArray = resp.data
    },
    //开始拖拽事件
    onStart() {
      this.drag = true
    },
    //拖拽结束事件
    onEnd() {
      this.drag = false
    },
    deleteItem(id) {
      this.$confirm('此操作将删除该列，不会显示在表格中, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.dataArray = this.dataArray.filter(item => item.field != id)
      })
    },
    saveFieldConfig() {
      // 保存配置信息
      this.$http.post(this.$api.advanced_tbls_save_fieldconfigs, { tblid: this.tblid, dataArray: this.dataArray })
      this.$router.push('/advanced/cleaning/index')
    }
  }
}
</script>
