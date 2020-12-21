<template>
  <div class="main">
    <el-row>
      <el-col :span="12" :offset="6">
        <el-tabs type="border-card" value="1">
          <el-tab-pane name="1" label="全部">
            <el-button @click="add_ds_form('excel')">添加Excel</el-button>
            <el-button @click="add_ds_form('csv')">添加csv</el-button>
            <el-button @click="add_ds_form('tsv')">添加tsv</el-button>
            <el-button @click="add_ds_form('mysql')">连接MySQL</el-button>
            <el-button @click="add_ds_form('http://www.weather.com.cn/textFC/hb.shtml')">中国天气 http://www.weather.com.cn/textFC/hb.shtml#</el-button>
            <el-button @click="add_ds_form('http://ir.nsfc.gov.cn/')">中国基金委 http://ir.nsfc.gov.cn/</el-button>
            <el-button @click="add_ds_form('https://www.nsf.gov/publications/')">美国国家科学基金委 https://www.nsf.gov/publications/</el-button>
            <el-button @click="add_ds_form('https://www.defense.gov/Explore/News/Listing/')">美国国防部新闻 https://www.defense.gov/Explore/News/Listing/</el-button>
          </el-tab-pane>
          <el-tab-pane name="2" label="外部文件">
            <el-button>添加Excel</el-button>
            <el-button>添加csv</el-button>
            <el-button>添加tsv</el-button>
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
    <el-drawer :title="drawerTitle" :visible.sync="drawerVisible" direction="rtl" ref="drawer">
      aaaaaaaaa
    </el-drawer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      drawerTitle: '',
      drawerVisible: false,
      uploadForm: {}
    }
  },
  computed: {},
  mounted() {},
  methods: {
    add_ds_form(name) {
      // 打开抽屉，数据源配置信息
      this.drawerTitle = '数据源：' + name
      this.drawerVisible = false
      this.doUpload()
    },
    async doUpload() {
      const { data: resp } = await this.$http.post(this.$api.advanced_upload, this.uploadForm)
      if (resp.status == 400) return this.$message.error(resp.msg)
      console.log('上传完成', resp)
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
