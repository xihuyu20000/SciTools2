<template>
  <div style="width:100%;margin-top:10px">
    <el-form :model="configForm">
      <el-row :gutter="20">
        <el-col :span="12" :offset="6">
          <el-collapse accordion>
            <el-collapse-item name="1">
              <template slot="title"><i class="header-icon el-icon-info"></i> <span class="title">停用词词典</span> </template>
              <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="configForm.stopwords_dict"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="2">
              <template slot="title"><span class="title">分词词典</span> </template>
              <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="stopwords_dict"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="3">
              <template slot="title"><span class="title">同义词词典</span> </template>
              <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="stopwords_dict"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="4">
              <template slot="title"><span class="title">国家和地区词典</span> </template>
              <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="stopwords_dict"> </el-input>
            </el-collapse-item>
          </el-collapse> </el-col
      ></el-row>
      <el-row :gutter="20" style="margin-top:10px">
        <el-col :span="2" :offset="11">
          <el-button type="primary" @click="submitForm('configForm')">保存</el-button>
        </el-col></el-row
      >
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      configForm: {
        stopwords_dict: ''
      }
    }
  },
  methods: {
    async submitForm() {
      const { data: resp } = await this.$http.post(this.$api.configSave, this.configForm)
      if (resp.status == 400) return this.$message.error(resp.msg)

      this.$notify({
        title: '登录成功',
        message: '欢迎登录系统',
        position: 'bottom-right',
        type: 'success'
      })
    },
    async fetch() {
      const { data: resp } = await this.$http.get(this.$api.configIndex)
      if (resp.status == 400) return this.$message.error(resp.msg)
      this.configForm = resp.data
    }
  },
  mounted() {
    this.fetch()
  }
}
</script>

<style lang="scss" scoped>
.title {
  font-size: 1.25em;
}
</style>
