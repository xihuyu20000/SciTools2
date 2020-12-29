<template>
  <div class="main">
    <el-row>
      <el-col :span="12" :offset="6">
        <el-tabs type="border-card" value="2">
          <el-tab-pane name="2" label="外部文件">
            <el-button @click="add_ds_form('excel')">添加Excel</el-button>
            <el-button @click="add_ds_form('csv')">添加csv</el-button>
            <el-button @click="add_ds_form('tsv')">添加tsv</el-button>
          </el-tab-pane>
          <el-tab-pane name="3" label="数据库"><el-button>连接MySQL</el-button></el-tab-pane>
          <el-tab-pane name="4" label="数据统计">
            <el-button>中国天气 http://www.weather.com.cn/textFC/hb.shtml#</el-button>
            <el-button>中国基金委 http://ir.nsfc.gov.cn/</el-button>
            <el-button>美国国家科学基金委 https://www.nsf.gov/publications/</el-button>
            <el-button>美国国防部新闻 https://www.defense.gov/Explore/News/Listing/</el-button>
          </el-tab-pane>
        </el-tabs>
      </el-col>
    </el-row>
    <vxe-modal v-model="uploadVisible" width="600">
      <template v-slot>
        <div>
          <el-row>
            <el-col :span="16" :offset="4">
              <el-form :model="form" ref="form" :rules="rules" label-width="80px" label-position="left">
                <el-form-item label="上传文件" prop="files">
                  <el-upload multiple :limit="1" action="string" list-type="text" :file-list="fileList" :auto-upload="false" :on-change="OnChange" :on-remove="OnRemove" :on-preview="handlePictureCardPreview" :before-remove="beforeRemove" :accept="acceptFiles">
                    <el-button size="small" type="primary">选择数据文件</el-button>
                    <div slot="tip" class="el-upload__tip" style="color:green">只能上传{{ acceptFiles }}格式</div>
                  </el-upload>
                </el-form-item>
                <el-form-item>
                  <el-button type="success" @click="onSubmit">开始上传</el-button>
                </el-form-item>
              </el-form>
            </el-col>
          </el-row>
        </div>
      </template>
    </vxe-modal>
  </div>
</template>

<script>
export default {
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
      },
      uploadVisible: false,
      acceptFiles: '.zip',
      uploadForm: {}
    }
  },
  computed: {},
  mounted() {},
  methods: {
    add_ds_form(name) {
      if (name == 'excel') {
        this.acceptFiles = '.xls'
      } else if (name == 'csv') {
        this.acceptFiles = '.csv'
      } else if (name == 'tsv') {
        this.acceptFiles = '.tsv'
      }
      this.form.style = name
      this.uploadVisible = true
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
      let loader = this.$loading.show({ container: null, canCancel: false })

      let _form = this.form
      for (let x in _form) {
        this.param.append(x, _form[x])
      }
      this.param.append('files', this.fileList[0].raw)
      const { data: resp } = await this.$http.post(this.$api.advanced_upload, this.param)
      if (resp.status != 200) return this.$message.error('上传失败')
      this.$refs['form'].resetFields()
      this.fileList = []
      loader.hide()
      this.uploadVisible = false
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
    },
    async doUpload() {
      const { data: resp } = await this.$http.post(this.$api.advanced_upload, this.uploadForm)
      if (resp.status == 400) return this.$message.error(resp.msg)
      // console.log('上传完成', resp)
      return this.$message.error('上传完成.....')
    }
  }
}
</script>

<style lang="scss" scoped>
.main {
  width: 100%;
  height: 100vh;
}
</style>
