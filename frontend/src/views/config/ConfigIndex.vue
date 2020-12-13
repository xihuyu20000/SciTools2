<template>
  <div style="width:100%;">
    <el-form :model="configForm">
      <el-row :gutter="20" style="margin-bottom:10px">
        <el-col :span="12" :offset="6">
          <el-collapse accordion>
            <el-collapse-item name="1">
              <template slot="title">
                <span class="title"><i class="header-icon el-icon-info"></i> 停用词词典</span>
                <el-radio-group v-model="configForm.stopwords_style" class="title-radio-group">
                  <el-radio :label="0">系统默认</el-radio>
                  <el-radio :label="1">使用自定义</el-radio><el-radio :label="2">系统默认合并自定义</el-radio>
                </el-radio-group>
              </template>
              <el-input type="textarea" v-model="configForm.stopwords_text" :rows="4" placeholder="书写时，每行一个"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="2">
              <template slot="title">
                <span class="title">分词词典</span>
                <el-radio-group v-model="configForm.splitwords_style" class="title-radio-group">
                  <el-radio :label="0">系统默认</el-radio>
                  <el-radio :label="1">使用自定义</el-radio><el-radio :label="2">系统默认合并自定义</el-radio>
                </el-radio-group>
              </template>
              <el-input type="textarea" v-model="configForm.splitwords_text" :rows="4" placeholder="书写时，每行一个"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="3">
              <template slot="title"
                ><span class="title">同义词词典</span>
                <el-radio-group v-model="configForm.synonymwords_style" class="title-radio-group">
                  <el-radio :label="0">系统默认</el-radio>
                  <el-radio :label="1">使用自定义</el-radio><el-radio :label="2">系统默认合并自定义</el-radio>
                </el-radio-group>
              </template>
              <el-input type="textarea" v-model="configForm.synonymwords_text" :rows="4" placeholder="书写时，同义词1;同义词2=同义词3"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="4">
              <template slot="title"
                ><span class="title">著者合并词典</span>
                <el-radio-group v-model="configForm.combineauthor_style" class="title-radio-group">
                  <el-radio :label="0">系统默认</el-radio>
                  <el-radio :label="1">使用自定义</el-radio><el-radio :label="2">系统默认合并自定义</el-radio>
                </el-radio-group>
              </template>
              <el-input type="textarea" v-model="configForm.combineauthor_text" :rows="4" placeholder="书写时，著者1,单位1;著者2,单位2=著者3,单位3"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="5">
              <template slot="title">
                <span class="title">机构合并词典</span>
                <el-radio-group v-model="configForm.combineorg_style" class="title-radio-group">
                  <el-radio :label="0">系统默认</el-radio>
                  <el-radio :label="1">使用自定义</el-radio><el-radio :label="2">系统默认合并自定义</el-radio>
                </el-radio-group>
              </template>
              <el-input type="textarea" v-model="configForm.combineorg_text" :rows="4" placeholder="书写时，单位1;单位2=单位3"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="6">
              <template slot="title">
                <span class="title">地区合并词典</span>
                <el-radio-group v-model="configForm.combineprovince_style" class="title-radio-group">
                  <el-radio :label="0">系统默认</el-radio>
                  <el-radio :label="1">使用自定义</el-radio><el-radio :label="2">系统默认合并自定义</el-radio>
                </el-radio-group>
              </template>
              <el-input type="textarea" v-model="configForm.combineprovince_text" :rows="4" placeholder="书写时，地区1;地区2=地区3"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="7">
              <template slot="title">
                <span class="title">国家合并词典</span>
                <el-radio-group v-model="configForm.combinecountry_style" class="title-radio-group">
                  <el-radio :label="0">系统默认</el-radio>
                  <el-radio :label="1">使用自定义</el-radio><el-radio :label="2">系统默认合并自定义</el-radio>
                </el-radio-group>
              </template>
              <el-input type="textarea" v-model="configForm.combinecountry_text" :rows="4" placeholder="书写时，国家1;国家2=国家3"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="8">
              <template slot="title">
                <span class="title">基金合并词典</span>
                <el-radio-group v-model="configForm.combinefund_style" class="title-radio-group">
                  <el-radio :label="0">系统默认</el-radio>
                  <el-radio :label="1">使用自定义</el-radio><el-radio :label="2">系统默认合并自定义</el-radio>
                </el-radio-group>
              </template>
              <el-input type="textarea" v-model="configForm.combinefund_text" :rows="4" placeholder="书写时，基金1;基金2=基金3"> </el-input>
            </el-collapse-item>
            <el-collapse-item name="9">
              <template slot="title">
                <span class="title">学科分类词典</span>
                <el-radio-group v-model="configForm.combinebranch_style" class="title-radio-group">
                  <el-radio :label="0">系统默认</el-radio>
                  <el-radio :label="1">使用自定义</el-radio><el-radio :label="2">系统默认合并自定义</el-radio>
                </el-radio-group>
              </template>
              <el-input type="textarea" v-model="configForm.combinebranch_text" :rows="4" placeholder="书写时，每行一个"> </el-input>
            </el-collapse-item>
          </el-collapse>
        </el-col>
      </el-row>
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
      configForm: {
        stopwords_style: 0,
        stopwords_text: '',

        splitwords_style: 0,
        splitwords_text: '',
        
        synonymwords_style: 0,
        synonymwords_text: '',
        
        combineauthor_style: 0,
        combineauthor_text: '',
        
        combineorg_style: 0,
        combineorg_text: '',

        combineprovince_style: 0,
        combineprovince_text: '',

        combinecountry_style: 0,
        combinecountry_text: '',

        combinefund_style: 0,
        combinefund_text: '',

        combinebranch_style: 0,
        combinebranch_text: '',

        kw_freq_style: '',
        kw_freq_value: 1
      },
      kw_freq_options: [
        {
          value: 'kw_freq_max',
          label: '最大词频'
        },
        {
          value: 'kw_freq_min',
          label: '最少词频'
        }
      ]
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
  width: 200px;
  display: inline-block;
}
.title-radio-group {
  margin-left: 50px;
}
</style>
