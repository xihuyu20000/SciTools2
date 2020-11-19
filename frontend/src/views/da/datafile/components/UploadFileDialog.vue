<template>
  <div>
    <el-dialog title="上传数据文件" width="650px" height="650px" :visible="uploadDialogVisible" :before-close="handleClose">
      <el-form :model="form" ref="form" :rules="rules" label-width="100px" label-position="right">
        <el-form-item label="数据来源" prop="source">
          <el-radio-group v-model="form.source">
            <el-radio label="cnki_custom">CNKI——知网导出自定义格式</el-radio><br />
            <el-radio label="cnkicite_custom">CNKI引文——知网引文导出自定义格式</el-radio><br />
            <el-radio label="cssci">CSSCI——中文社会科学引文索引</el-radio><br />
            <el-radio label="wos_text">WOS——Web of Science导出纯文本格式</el-radio><br />
          </el-radio-group>
        </el-form-item>
        <el-form-item prop="files">
          <el-upload multiple :limit="1" action="string" list-type="text" :file-list="fileList" :auto-upload="false" :on-change="OnChange" :on-remove="OnRemove" :on-preview="handlePictureCardPreview" :before-remove="beforeRemove" accept=".zip">
            <el-button size="small" type="primary">选择数据文件</el-button>
            <div slot="tip" class="el-upload__tip" style="color:green">只能上传zip格式，如果是多个文件，请压缩到一起再上传</div></el-upload
          >
        </el-form-item>
        <el-form-item label="任务名称" prop="name">
          <input v-model="form.name" />
        </el-form-item>
        <el-form-item>
          <el-button type="" @click="onSubmit">开始上传</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
export default {
  components: {},

  data() {
    var validateFiles = (rule, value, callback) => {
      if (this.fileList.length === 0) {
        callback(new Error('请选择数据文件'))
      } else {
        callback()
      }
    }
    return {
      uploadDialogVisible: false,
      param: new FormData(),
      form: {},
      count: 0,
      fileList: [],
      fileDialogVisible: false,
      dialogImageUrl: '',
      rules: {
        source: [{ required: true, message: '请输入来源', trigger: 'blur' }],
        files: [{ validator: validateFiles, trigger: 'blur' }],
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
      }
    }
  },
  methods: {
    handleClose() {
      this.uploadDialogVisible = false
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url
      this.fileDialogVisible = true
    },
    // eslint-disable-next-line no-unused-vars
    beforeRemove(file, fileList) {
      return this.$confirm(`确定移除 ${file.name}？`)
    },
    // eslint-disable-next-line no-unused-vars
    OnChange(file, fileList) {
      this.fileList = fileList
    },
    OnRemove(file, fileList) {
      this.fileList = fileList
    },
    async submit() {
      let _form = this.form
      for (let x in _form) {
        this.param.append(x, _form[x])
      }
      this.param.append('files', this.fileList[0].raw)
      const { data: resp } = await this.$http.post('/file/upload', this.param)
      if (resp.status != 200) return this.$message.error('上传失败')
      this.$bus.$emit('completeUploadFiles', resp.data)
      this.uploadDialogVisible = false

      this.$refs['form'].resetFields()
      this.fileList = []
    },
    onSubmit() {
      let _this = this
      this.$refs['form'].validate(function(valid) {
        if (!valid) return false
        _this.submit()
      })
    }
  },
  mounted: function() {
    this.$bus.$on('showUploadDialog', () => {
      this.uploadDialogVisible = true
    })
  }
}
</script>
<style></style>
