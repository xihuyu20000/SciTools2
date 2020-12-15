<template>
  <el-container>
    <el-aside width="300px">
      <div>
        <el-menu default-active="2" class="el-menu-vertical-demo" @select="selectMenu">
          <div style="display:flex;justify-content:flex-end;">
            <span>数据集：</span>
            <el-select v-model="target_dataset" placeholder="请选择" @change="chooseDataset">
              <el-option v-for="item in datasets" :key="item.dsid" :label="item.dsname" :value="item.dsid"> </el-option>
            </el-select>
          </div>
          <el-submenu :index="index + ''" v-for="(item, index) in menu" :key="index">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>{{ item.title }}（{{ item.children.length }}）</span>
            </template>
            <el-menu-item :index="sub.path" v-for="(sub, index) in item.children" :key="index">【{{ index + 1 }}】{{ sub.title }}</el-menu-item>
          </el-submenu>
        </el-menu>
      </div>
    </el-aside>
    <el-main><router-view /></el-main>
  </el-container>
</template>

<script>
export default {
  data: function() {
    return {
      target_dataset: '',
      datasets: [],
      menu: [
        {
          title: '基础指标',
          children: [
            { title: '历年发文量', path: '/stat/statArticlesByYear' },
            { title: '国家发文量', path: '/stat/statArticlesByCountry' },
            { title: '地区发文量', path: '/stat/statArticlesByProvince' },
            { title: '机构发文量', path: '/stat/statArticlesByOrg' },
            { title: '一作发文量', path: '/stat/statArticlesByFirstDuty' },
            { title: '作者发文量', path: '/stat/statArticlesByAuthor' },
            { title: '来源发文量', path: '/stat/statArticlesByJournal' },
            { title: '基金支持统计', path: '/stat/statArticlesByFund' },
            { title: '基金类型统计', path: '/stat/statStyleByFund' },
            { title: '学科分布', path: '/stat/statArticlesBySubject' },
            { title: '合著人数统计', path: '/stat/statPersonsByCoAuthor' },
            { title: '关键词词频', path: '/stat/statKwsByCount' }
          ]
        },
        {
          title: '绘制词云',
          children: [{ title: '关键词', path: '/wordclound/keyword' }]
        },
        {
          title: '共现指标',
          children: [
            { title: '关键词共现矩阵', path: '/coocMatrix/keyword' },
            { title: '主题词共现矩阵', path: '/coocMatrix/topicword' },
            { title: '作者共现矩阵', path: '' },
            { title: '基金共现矩阵', path: '' },
            { title: '机构共现矩阵', path: '' },
            { title: '国家共现矩阵', path: '' }
          ]
        },
        {
          title: '散点图',
          children: [
            { title: '共现关键词散点图', path: '/scatter/coockeyword' },
            { title: '共现主题词散点图', path: '/scatter/cooctopicword' }
          ]
        },
        {
          title: '网络聚类',
          children: [
            { title: '关键词谱聚类', path: '/cluster/spectral/keyword' },
            { title: '关键词层次聚类', path: '/cluster/hierarchy/keyword' },
            { title: '关键词聚类趋势', path: '/cluster/trend/keyword' }
          ]
        },
        {
          title: '知识图谱',
          children: [
            { title: '全局图谱', path: '/kg/index' },
            { title: '知识搜索', path: '/kg/search' },
            { title: '知识关联', path: '/kg/connect' }
          ]
        },
        { title: '作者评价', children: [{ title: '', path: '' }] },
        { title: '机构评价', children: [{ title: '', path: '' }] },
        { title: '国家评价', children: [{ title: '', path: '' }] },
        { title: '期刊评价', children: [{ title: '', path: '' }] }
      ]
    }
  },
  created() {
    this.fetch()
    this.target_dataset = sessionStorage.getItem('target_dataset')
  },
  methods: {
    async fetch() {
      let _url = this.$api.dataset_list_names
      const { data: resp } = await this.$http.get(_url)
      if (resp.status == 400) return this.$message.error(resp.msg)
      this.datasets = resp.data
    },
    chooseDataset(item) {
      sessionStorage.setItem('target_dataset', item)
    },
    selectMenu(index) {
      if (this.target_dataset == '')
        return this.$notify({
          title: '警告',
          message: '请选择数据集',
          type: 'warning',
          position: 'top-left'
        })
      this.$router.push({
        path: index + `/${this.target_dataset}`
      })
    }
  },
  components: {}
}
</script>

<style lang="scss" scoped>
.main {
  width: 100%;
}
</style>
