<template>
  <el-container>
    <el-aside width="300px">
      <div>
        <el-tag type="info" size="medium">数据集：</el-tag><el-cascader :options="datasets" :show-all-levels="false"></el-cascader>
        <el-menu :router="true" default-active="2" class="el-menu-vertical-demo">
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
      datasets: [
        {
          value: 'zhinan',
          label: '数字人文',
          children: [
            {
              value: 'shejiyuanze',
              label: '1900-2020年'
            }
          ]
        }
      ],
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
            { title: '关键词词频', path: '/stat/statKwsByCount' },
            { title: '主题词词频', path: '/stat/statTwsByCount' }
          ]
        },
        {
          title: '绘制词云',
          children: [
            { title: '关键词', path: '/wordclound/keyword' },
            { title: '主题词', path: '/wordclound/topicword' }
          ]
        },
        {
          title: '共现指标',
          children: [
            { title: '关键词共现矩阵', path: '' },
            { title: '主题词共现矩阵', path: '' },
            { title: '作者共现矩阵', path: '' },
            { title: '基金共现矩阵', path: '' },
            { title: '机构共现矩阵', path: '' },
            { title: '国家共现矩阵', path: '' }
          ]
        },
        { title: '网络聚类', children: [{ title: '', path: '' }] },
        { title: '知识图谱', children: [{ title: '', path: '' }] },
        { title: '作者评价', children: [{ title: '', path: '' }] },
        { title: '机构评价', children: [{ title: '', path: '' }] },
        { title: '国家评价', children: [{ title: '', path: '' }] },
        { title: '期刊评价', children: [{ title: '', path: '' }] }
      ]
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
