import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/common/Home.vue'
import Default from '@/views/common/Default.vue'
import Login from '@/views/common/Login.vue'
import V404 from '@/views/common/404.vue'

import AdvancedIndex from '@/views/advanced/AdvancedIndex.vue'
import AdvancedCleaningIndex from '@/views/advanced/CleaningIndex.vue'
import AdvancedDatasourceIndex from '@/views/advanced/DatasourceIndex.vue'
import AdvancedGraphIndex from '@/views/advanced/GraphIndex.vue'

import ConfigIndex from '@/views/config/ConfigIndex.vue'
import ReportIndex from '@/views/report/ReportIndex.vue'

import circularGraphForKeyWord from '@/views/scimetrics-stat/components/circularGraphForKeyWord.vue'
import clusterBurstingForKeyWord from '@/views/scimetrics-stat/components/clusterBurstingForKeyWord.vue'
import clusterHierarchyForKeyWord from '@/views/scimetrics-stat/components/clusterHierarchyForKeyWord.vue'
import clusterSpectralForKeyWord from '@/views/scimetrics-stat/components/clusterSpectralForKeyWord.vue'
import clusterTrendForKeyWord from '@/views/scimetrics-stat/components/clusterTrendForKeyWord.vue'

import coocMatrixForAuthor from '@/views/scimetrics-stat/components/coocMatrixForAuthor.vue'
import coocMatrixForCountry from '@/views/scimetrics-stat/components/coocMatrixForCountry.vue'
import coocMatrixForFund from '@/views/scimetrics-stat/components/coocMatrixForFund.vue'
import coocMatrixForKeyWord from '@/views/scimetrics-stat/components/coocMatrixForKeyWord.vue'
import coocMatrixForOrg from '@/views/scimetrics-stat/components/coocMatrixForOrg.vue'

import kgConnect from '@/views/scimetrics-stat/components/kgConnect'
// import kgIndexHtml from '@/views/scimetrics-stat/components/kgIndex.html'
import kgIndex from '@/views/scimetrics-stat/components/kgIndex'
import kgSearch from '@/views/scimetrics-stat/components/kgSearch'

import scatterCoocKeyWord from '@/views/scimetrics-stat/components/scatterCoocKeyWord.vue'

import ScimetricsIndex from '@/views/scimetrics/ScimetricsIndex.vue'
import ScimetricsDataSourceIndex from '@/views/scimetrics/ScimetricsDataSourceIndex.vue'
import ScimetricsCleaningIndex from '@/views/scimetrics/ScimetricsCleaningIndex.vue'
import ScimetricsGraphIndex from '@/views/scimetrics-stat/ScimetricsGraphIndex.vue'

import statArticlesByAuthor from '@/views/scimetrics-stat/components/statArticlesByAuthor.vue'
import statArticlesByCountry from '@/views/scimetrics-stat/components/statArticlesByCountry.vue'
import statArticlesByFirstDuty from '@/views/scimetrics-stat/components/statArticlesByFirstDuty.vue'
import statArticlesByFund from '@/views/scimetrics-stat/components/statArticlesByFund.vue'
import statArticlesByJournal from '@/views/scimetrics-stat/components/statArticlesByJournal.vue'
import statArticlesByOrg from '@/views/scimetrics-stat/components/statArticlesByOrg.vue'
import statArticlesByProvince from '@/views/scimetrics-stat/components/statArticlesByProvince.vue'
import statArticlesBySubject from '@/views/scimetrics-stat/components/statArticlesBySubject.vue'
import statArticlesByYear from '@/views/scimetrics-stat/components/statArticlesByYear.vue'
import statKwsByCount from '@/views/scimetrics-stat/components/statKwsByCount.vue'
import statPersonsByCoAuthor from '@/views/scimetrics-stat/components/statPersonsByCoAuthor.vue'

import wordCloundForKeyWord from '@/views/scimetrics-stat/components/wordCloundForKeyWord.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    children: [
      { path: '/', redirect: '/default' },
      {
        path: '/default',
        name: '首页',
        component: Default
      },

      {
        path: '/advanced/index',
        name: '高级图表',
        component: AdvancedIndex,
        children: [
          {
            path: '/advanced/datasource/index',
            name: '高级数据源首页',
            component: AdvancedDatasourceIndex
          },
          {
            path: '/advanced/cleaning/index',
            name: '高级数据清洗首页',
            component: AdvancedCleaningIndex
          },
          {
            path: '/advanced/graph/index',
            name: '高级图表展现首页',
            component: AdvancedGraphIndex
          }
        ]
      },
      {
        path: '/scimetrics/scimetricsIndex',
        name: '科学计量',
        component: ScimetricsIndex,
        children: [
          {
            path: '/scimetrics/datasource/index',
            name: '科学计量数据源',
            component: ScimetricsDataSourceIndex
          },
          {
            path: '/scimetrics/cleaning/index',
            name: '科学计量数据清洗',
            component: ScimetricsCleaningIndex
          },
          {
            path: '/scimetrics/graph/index',
            name: '科学计量图表展现首页',
            component: ScimetricsGraphIndex,
            children: [
              {
                path: '/circularGraph/keyword/:dsid',
                name: '关键词共现关系图',
                component: circularGraphForKeyWord
              },
              {
                path: '/cluster/bursting/keyword/:dsid',
                name: '关键词突现图谱',
                component: clusterBurstingForKeyWord
              },
              {
                path: '/cluster/hierarchy/keyword/:dsid',
                name: '关键词层级聚类',
                component: clusterHierarchyForKeyWord
              },
              {
                path: '/cluster/spectral/keyword/:dsid',
                name: '关键词谱聚类',
                component: clusterSpectralForKeyWord
              },
              {
                path: '/cluster/trend/keyword/:dsid',
                name: '关键词聚类趋势',
                component: clusterTrendForKeyWord
              },
              {
                path: '/coocMatrix/author/:dsid',
                name: '作者共现矩阵',
                component: coocMatrixForAuthor
              },
              {
                path: '/coocMatrix/country/:dsid',
                name: '国家共现矩阵',
                component: coocMatrixForCountry
              },
              {
                path: '/coocMatrix/fund/:dsid',
                name: '基金共现矩阵',
                component: coocMatrixForFund
              },
              {
                path: '/coocMatrix/keyword/:dsid',
                name: '关键词共现矩阵',
                component: coocMatrixForKeyWord
              },
              {
                path: '/coocMatrix/org/:dsid',
                name: '机构共现矩阵',
                component: coocMatrixForOrg
              },
              {
                path: '/kg/connect/:dsid',
                name: '知识关联',
                component: kgConnect
              },
              {
                path: '/kg/index/:dsid',
                name: '全局图谱',
                component: kgIndex
              },
              {
                path: '/kg/search/:dsid',
                name: '知识搜索',
                component: kgSearch
              },
              {
                path: '/scatter/coockeyword/:dsid',
                name: '共现关键词散点图',
                component: scatterCoocKeyWord
              },
              {
                path: '/scimetrics-stat/statArticlesByAuthor/:dsid',
                name: '作者发文量',
                component: statArticlesByAuthor
              },
              {
                path: '/scimetrics-stat/statArticlesByCountry/:dsid',
                name: '国家发文量',
                component: statArticlesByCountry
              },
              {
                path: '/scimetrics-stat/statArticlesByFirstDuty/:dsid',
                name: '一作发文量',
                component: statArticlesByFirstDuty
              },
              {
                path: '/scimetrics-stat/statArticlesByFund/:dsid',
                name: '基金支持发文量',
                component: statArticlesByFund
              },
              {
                path: '/scimetrics-stat/statArticlesByJournal/:dsid',
                name: '期刊来源统计',
                component: statArticlesByJournal
              },
              {
                path: '/scimetrics-stat/statArticlesByOrg/:dsid',
                name: '机构发文量',
                component: statArticlesByOrg
              },
              {
                path: '/scimetrics-stat/statArticlesByProvince/:dsid',
                name: '地区发文量',
                component: statArticlesByProvince
              },
              {
                path: '/scimetrics-stat/statArticlesByJournal/:dsid',
                name: '期刊发文量',
                component: statArticlesByJournal
              },
              {
                path: '/scimetrics-stat/statArticlesBySubject/:dsid',
                name: '学科分布统计',
                component: statArticlesBySubject
              },
              {
                path: '/scimetrics-stat/statArticlesByYear/:dsid',
                name: '历年发文量',
                component: statArticlesByYear
              },
              {
                path: '/scimetrics-stat/statKwsByCount/:dsid',
                name: '关键词词频',
                component: statKwsByCount
              },
              {
                path: '/scimetrics-stat/statPersonsByCoAuthor/:dsid',
                name: '合著人数统计',
                component: statPersonsByCoAuthor
              },
              {
                path: '/wordclound/keyword/:dsid',
                name: '关键词词频',
                component: wordCloundForKeyWord
              }
            ]
          }
        ]
      },

      {
        path: '/report/index',
        name: '生成报告',
        component: ReportIndex
      },
      {
        path: '/config/index',
        name: '配置信息',
        component: ConfigIndex
      }
    ]
  },
  {
    path: '/login',
    name: '登录',
    component: Login
  },
  {
    path: '*',
    component: V404
  }
]

// const requireComponent = require.context('../views/common/template/', false, /.*\.vue$/)
// requireComponent.keys().forEach(fileName => {
//   console.log('加载', fileName, require('@/views/common/template/A.vue'))
// })

const router = new VueRouter({
  routes
})

import NProgress from 'nprogress'
import 'nprogress/nprogress.css'

router.beforeEach((to, from, next) => {
  NProgress.start()
  // console.log("from", from);
  // 获取token
  const token = sessionStorage.getItem('token')
  // 如果是登录或者有token，则通过
  if (to.path === '/login' || token) return next()
  console.error('未授权用户，请登录')
  next('/login')
})
router.afterEach(() => {
  NProgress.done()
})
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

export default router
