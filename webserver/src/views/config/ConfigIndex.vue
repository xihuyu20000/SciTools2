<template>
  <div style="width:100%;">
    <el-form :model="configForm">
      <el-row :gutter="20" style="margin-bottom:10px">
        <el-col :span="12" :offset="6">
          <el-collapse accordion>
            <el-collapse-item name="1">
              <template slot="title"><i class="header-icon el-icon-info"></i> <span class="title">停用词词典</span> </template>
              <el-input type="textarea" :rows="4" placeholder="请输入内容"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="2">
              <template slot="title"><span class="title">分词词典</span> </template>
              <el-input type="textarea" :rows="4" placeholder="请输入内容"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="3">
              <template slot="title"><span class="title">同义词词典</span> </template>
              <el-input type="textarea" :rows="4" placeholder="请输入内容"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="4">
              <template slot="title"><span class="title">人名词典</span> </template>
              <el-input type="textarea" :rows="4" placeholder="请输入内容"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="5">
              <template slot="title"><span class="title">机构词典</span> </template>
              <el-input type="textarea" :rows="4" placeholder="请输入内容"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="6">
              <template slot="title"><span class="title">地区词典</span> </template>
              <el-input type="textarea" :rows="4" placeholder="请输入内容"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="7">
              <template slot="title"><span class="title">国家词典</span> </template>
              <el-input type="textarea" :rows="4" placeholder="请输入内容"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="8">
              <template slot="title"><span class="title">学科大类词典</span> </template>
              <el-input type="textarea" :rows="4" placeholder="请输入内容"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="9">
              <template slot="title"><span class="title">学科小类词典</span> </template>
              <el-input type="textarea" :rows="4" placeholder="请输入内容"> </el-input>
            </el-collapse-item> </el-collapse></el-col
      ></el-row>
      <el-row :gutter="20">
        <el-col :span="12" :offset="6">
          <el-collapse accordion>
            <el-collapse-item name="1">
              <template slot="title"><span class="title">关键词统计数量</span> </template>
              <el-select v-model="configForm.kw_freq_style" placeholder="请选择"> <el-option v-for="item in kw_freq_options" :key="item.value" :label="item.label" :value="item.value"> </el-option> </el-select><el-input placeholder="关键词统计数量" v-model="configForm.kw_freq_value"> </el-input>
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
      kw_freq_options: [
        {
          value: 'kw_freq_max',
          label: '最大词频'
        },
        {
          value: 'kw_freq_min',
          label: '最少词频'
        }
      ],
      configForm: {
        stopwords_dict: '',
        kw_freq_style: '',
        kw_freq_value: 1
      }
    }
  },
  methods: {
    async submitForm() {
      const { data: resp } = await this.$http.post(this.$api.config_save, this.configForm)
      if (resp.status == 400) return this.$message.error(resp.msg)

      this.$notify({
        title: '保存成功',
        message: '可以在分析数据时自动使用配置',
        position: 'bottom-right',
        type: 'success'
      })
    },
    async fetch() {
      const { data: resp } = await this.$http.get(this.$api.config)
      if (resp.status == 400) return this.$message.error(resp.msg)
      this.configForm = resp.data
    },
    reload() {
      // 清除所有状态
      this.$refs.xTree.clearAll()
      return this.fetch()
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
