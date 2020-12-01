<template>
  <div style="width:100%;margin-top:100px">
    <el-row :gutter="20">
      <el-col :span="12" :offset="6">
        <el-form :model="form" ref="form" :rules="rules" label-width="100px" label-position="right">
          <el-form-item prop="files">
            <el-upload multiple :limit="1" action="string" list-type="text" :file-list="fileList" :auto-upload="false" :on-change="OnChange" :on-remove="OnRemove" :on-preview="handlePictureCardPreview" :before-remove="beforeRemove" accept=".zip">
              <el-button size="small" type="primary">选择数据文件</el-button>
              <div slot="tip" class="el-upload__tip" style="color:green">只能上传zip格式，如果是多个文件，请压缩到一起再上传</div></el-upload
            >
          </el-form-item>
          <el-form-item>
            <el-button type="" @click="onSubmit">开始上传</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
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
      param: new FormData(),
      form: {},
      count: 0,
      fileList: [],
      fileDialogVisible: false,
      dialogImageUrl: '',
      rules: {
        files: [{ validator: validateFiles, trigger: 'blur' }]
      }
    }
  },
  methods: {
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
      const { data: resp } = await this.$http.post(this.$api.upload, this.param)
      if (resp.status != 200) return this.$message.error('上传失败')
      this.$refs['form'].resetFields()
      this.fileList = []
      this.$message.success('上传成功')
      this.$router.push('/to/showing/index')
    },
    onSubmit() {
      let _this = this
      this.$refs['form'].validate(function(valid) {
        if (!valid) return false
        _this.submit()
      })
    }
  }
}
</script>
<style lang="scss" scoped>
.grid-content {
  min-height: 100vh;
}
.bg-purple {
  background: #d3dce6;
}
</style>
