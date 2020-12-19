<template>
  <el-container>
    <el-aside width="300px">
      <div>
        <el-menu class="el-menu-vertical-demo" @select="selectMenu">
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
            { title: '期刊发文量', path: '/stat/statArticlesByJournal' },
            { title: '一作发文量', path: '/stat/statArticlesByFirstDuty' },
            { title: '作者发文量', path: '/stat/statArticlesByAuthor' },
            { title: '基金类型统计', path: '/stat/statArticlesByFund' },
            // { title: '学科分布', path: '/stat/statArticlesBySubject' },
            { title: '合作人数统计', path: '/stat/statPersonsByCoAuthor' },
            { title: '关键词词频', path: '/stat/statKwsByCount' }
          ]
        },
        // {
        //   title: '绘制词云',
        //   children: [{ title: '关键词', path: '/wordclound/keyword' }]
        // },
        {
          title: '共现关系',
          children: [
            { title: '关键词共现矩阵', path: '/coocMatrix/keyword' },
            { title: '关键词共现散点图', path: '/scatter/coockeyword' },
            { title: '关键词共现关系图', path: '/circularGraph/coockeyword' },
            { title: '作者共现矩阵', path: '/coocMatrix/author' },
            { title: '基金共现矩阵', path: '/coocMatrix/fund' },
            { title: '机构共现矩阵', path: '/coocMatrix/org' },
            { title: '国家共现矩阵', path: '/coocMatrix/country' }
          ]
        },
        // {
        //   title: '引证关系',
        //   children: [{ title: '也就是引用和被引用', path: '' }]
        // },
        // {
        //   title: '关联关系',
        //   children: [{ title: '也就是引用和被引用', path: '' }]
        // },
        {
          title: '网络聚类',
          children: [
            { title: '关键词谱聚类', path: '/cluster/spectral/keyword' },
            { title: '关键词层次聚类', path: '/cluster/hierarchy/keyword' },
            { title: '关键词演化趋势', path: '/cluster/trend/keyword' },
            { title: '关键词突现图谱', path: '/cluster/bursting/keyword' }
          ]
        },
        {
          title: '知识图谱',
          children: [
            { title: '全局图谱', path: '/kg/index' },
            { title: '知识搜索', path: '/kg/search' },
            { title: '知识关联', path: '/kg/connect' }
          ]
        }
        // { title: '作者评价', children: [{ title: 'aa', path: '' }] },
        // { title: '机构评价', children: [{ title: 'aa', path: '' }] },
        // { title: '国家评价', children: [{ title: 'aa', path: '' }] },
        // { title: '期刊评价', children: [{ title: 'aa', path: '' }] }
      ]
    }
  },
  created() {
    this.fetch()
    // 加载会话中的数据
    let _target_dataset = sessionStorage.getItem('target_dataset')
    if (_target_dataset != null) this.target_dataset = _target_dataset
  },
  methods: {
    async fetch() {
      const { data: resp } = await this.$http.get(this.$api.dataset_list_names)
      if (resp.status == 400) return this.$message.error(resp.msg)
      this.datasets = resp.data
    },
    chooseDataset(item) {
      // 选择数据集
      sessionStorage.setItem('target_dataset', item)
    },
    selectMenu(index) {
      // 点击菜单
      if (this.target_dataset == '') return this.$message.error('请选择数据集')
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
