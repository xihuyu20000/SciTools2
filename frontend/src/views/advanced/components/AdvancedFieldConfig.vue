<template>
  <!-- http://www.itxst.com/vue-draggable/tutorial.html -->
  <div class="main">
    <el-row :gutter="20" style="margin-top:50px">
      <el-col :offset="6" :span="12">
        <!--使用draggable组件-->
        <draggable v-model="dataArray" chosenClass="chosen" forceFallback="true" group="people" animation="1000" @start="onStart" @end="onEnd">
          <transition-group>
            <div class="item" v-for="element in dataArray" :key="element.id">
              <span>{{ element.label }}</span>
              <i class="el-icon-delete" @click="deleteItem(element.id)"></i>
            </div>
          </transition-group>
        </draggable>
      </el-col>
      <el-col :offset="11" :span="2">
        <el-button type="primary">生成报告</el-button>
      </el-col>
    </el-row>
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
  justify-content: space-between;
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
      //定义要被拖拽对象的数组
      dataArray: [
        { id: 1, label: '论文历年统计——图形' },
        { id: 2, label: '论文历年统计——表格' }
      ]
    }
  },
  created() {
    this.fetch()
  },
  methods: {
    async fetch() {
      const { data: resp } = await this.$http.get(this.$api.advanced_tbls_list_fieldconfigs)
      if (resp.status == 400) return this.$message.error(resp.msg)
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
      this.$confirm('此操作将删除该内容，不会添加到报告中, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.dataArray = this.dataArray.filter(item => item.id != id)
      })
    }
  }
}
</script>
