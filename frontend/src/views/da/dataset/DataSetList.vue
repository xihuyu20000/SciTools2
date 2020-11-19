<template>
  <div>
    <el-table :data="tableData" row-key="id" border default-expand-all>
      <el-table-column type="selection" width="55"> </el-table-column>
      <el-table-column prop="file_name" label="文件名称" width="200"> </el-table-column>
      <el-table-column prop="file_size" label="文件大小" width="200"> </el-table-column>
      <el-table-column prop="create_date" label="上传时间" width="200"> </el-table-column>
      <el-table-column prop="status" label="状态" width="200"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="warning" slot="reference" @click="showdataset(scope.$index, scope.row)">查看数据集</el-button>
          <slot name="row" :row="scope.row"></slot>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return { tableData: [] }
  },
  methods: {
    async fetch() {
      const { data: resp1 } = await this.$http.get('/dataset?datafile_id=' + this.$route.query.id)
      this.tableData = resp1.data
    },
    showdataset(index, row) {
      console.log('显示数据集应答', index, row)
    }
  },
  mounted: async function() {
    this.fetch()
  },
  components: {}
}
</script>

<style lang="scss" scoped></style>
