<template>
  <div>
    <el-button type="primary" @click="showUploadDialog">上传文件</el-button>
    <upload-file-dialog></upload-file-dialog>
    <el-table :data="tableData" row-key="id" border default-expand-all>
      <el-table-column type="selection" width="55"> </el-table-column>
      <el-table-column prop="file_name" label="文件名称" width="200"> </el-table-column>
      <el-table-column prop="file_size" label="文件大小" width="200"> </el-table-column>
      <el-table-column prop="create_date" label="上传时间" width="200"> </el-table-column>
      <el-table-column prop="status" label="状态" width="200"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="warning" slot="reference" v-if="scope.row.status == '解析成功'" @click="showdataset(scope.$index, scope.row)">查看数据集</el-button>
          <el-button type="primary" slot="reference" v-else @click="parse(scope.$index, scope.row)">解析数据</el-button>
          <el-button type="info" slot="reference" @click="exportExcel(scope.$index, scope.row)">导出excel</el-button>
          <el-popconfirm title="确定删除吗？" @onConfirm="handleDelete(scope.$index, scope.row)" style="margin-left:10px">
            <el-button type="danger" slot="reference">删除</el-button>
          </el-popconfirm>
          <slot name="row" :row="scope.row"></slot>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import UploadFileDialog from './components/UploadFileDialog'
export default {
  data() {
    return { tableData: [] }
  },
  methods: {
    showUploadDialog: function() {
      this.$bus.$emit('showUploadDialog')
    },
    async fetch() {
      const { data: resp1 } = await this.$http.get('/file/list/')
      this.tableData = resp1.data
    },
    showdataset(index, row) {
      window.localStorage.setItem('datafile_id', row.id)
      this.$router.push({ path: '/default' })
      // this.$router.push({ path: '/da/dataset/list', query: { id: row.id } })
    },
    async parse(index, row) {
      const { data: resp } = await this.$http.get('/datafile/parse/' + row.id)
      console.log('解析应答', resp)
    },
    async exportExcel(index, row) {
      await this.$http.get('/datafile/exportExcel/' + row.id, { responseType: 'arraybuffer' }).then(response => {
        //创建一个blob对象,file的一种
        let blob = new Blob([response.data], { type: 'application/x-zip-compressed' })
        let link = document.createElement('a')
        link.href = window.URL.createObjectURL(blob)
        //配置下载的文件名
        link.download = 'datafile.zip'
        link.click()
      })
    },
    async handleDelete(index, row) {
      const { data: resp } = await this.$http.delete('/file/' + row.id)
      console.log('删除', resp)
      if (resp.status == 200) {
        this.$message.success('删除成功')
        this.fetch()
      } else {
        this.$message.error('删除失败')
      }
    }
  },
  mounted: async function() {
    this.$bus.$on('completeUploadFiles', () => {
      this.$message.success('上传成功')
      this.uploadDialogVisible = false
      this.fetch()
    })
    this.fetch()
  },
  components: {
    UploadFileDialog
  }
}
</script>

<style lang="scss" scoped></style>
