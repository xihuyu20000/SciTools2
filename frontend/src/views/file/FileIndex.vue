<template>
  <div style="width:100%;margin-top:100px">
    <el-row :gutter="20">
      <el-col :span="12" :offset="6">
        <el-form :model="form" ref="form" :rules="rules" label-width="100px" label-position="right">
          <el-form-item label="内容类型" prop="style">
            <el-select v-model="form.style" placeholder="请选择类型">
              <el-option label="题录—国标—GBT 7714-2015" value="题录—国标—GBT 7714-2015"></el-option>
              <el-option label="题录—知网—es5" value="题录—知网—es5"></el-option>
              <el-option label="题录—知网—自定义格式" value="题录—知网—自定义格式"></el-option>
              <el-option label="题录—WOS—制表符分割" value="题录—WOS—制表符分割"></el-option>
              <el-option label="引文—cssci" value="引文—cssci"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="上传文件" prop="files">
            <el-upload multiple :limit="1" action="string" list-type="text" :file-list="fileList" :auto-upload="false" :on-change="OnChange" :on-remove="OnRemove" :on-preview="handlePictureCardPreview" :before-remove="beforeRemove" accept=".zip">
              <el-button size="small" type="primary">选择数据文件</el-button>
              <div slot="tip" class="el-upload__tip" style="color:green">只能上传zip格式，如果是多个文件，请压缩到一起再上传</div></el-upload
            >
          </el-form-item>
          <el-form-item>
            <el-button type="success" @click="onSubmit">开始上传</el-button>
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
      form: { style: '' },
      count: 0,
      fileList: [],
      fileDialogVisible: false,
      dialogImageUrl: '',
      rules: {
        style: [{ required: true, trigger: 'blur', message: '请选择文件类型' }],
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
      let loader = this.$loading.show({ container: null, canCancel: false })

      let _form = this.form
      for (let x in _form) {
        this.param.append(x, _form[x])
      }
      this.param.append('files', this.fileList[0].raw)
      const { data: resp } = await this.$http.post(this.$api.file_upload, this.param)
      if (resp.status != 200) return this.$message.error('上传失败')
      this.$refs['form'].resetFields()
      this.fileList = []
      loader.hide()
      return this.$notify({
        title: '成功',
        message: '导入成功',
        type: 'success'
      })
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
