import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/common/Home.vue'
import Default from '@/views/common/Default.vue'
import Login from '@/views/common/Login.vue'
import V404 from '@/views/common/404.vue'

import FileIndex from '@/views/file/FileIndex.vue'
import DatasetIndex from '@/views/dataset/DatasetIndex.vue'
import StatIndex from '@/views/stat/StatIndex.vue'
import ConfigIndex from '@/views/config/ConfigIndex.vue'

import clusterBurstingForKeyWord from '@/views/stat/components/clusterBurstingForKeyWord.vue'
import clusterHierarchyForKeyWord from '@/views/stat/components/clusterHierarchyForKeyWord.vue'
import clusterSpectralForKeyWord from '@/views/stat/components/clusterSpectralForKeyWord.vue'
import clusterTrendForKeyWord from '@/views/stat/components/clusterTrendForKeyWord.vue'

import coocMatrixForKeyWord from '@/views/stat/components/coocMatrixForKeyWord.vue'
import coocMatrixForTopicWord from '@/views/stat/components/coocMatrixForTopicWord.vue'

import kgConnect from '@/views/stat/components/kgConnect'
// import kgIndexHtml from '@/views/stat/components/kgIndex.html'
import kgIndex from '@/views/stat/components/kgIndex'
import kgSearch from '@/views/stat/components/kgSearch'

import scatterCoocKeyWord from '@/views/stat/components/scatterCoocKeyWord.vue'

import statArticlesByAuthor from '@/views/stat/components/statArticlesByAuthor.vue'
import statArticlesByCountry from '@/views/stat/components/statArticlesByCountry.vue'
import statArticlesByFirstDuty from '@/views/stat/components/statArticlesByFirstDuty.vue'
import statArticlesByFund from '@/views/stat/components/statArticlesByFund.vue'
import statArticlesByJournal from '@/views/stat/components/statArticlesByJournal.vue'
import statArticlesByOrg from '@/views/stat/components/statArticlesByOrg.vue'
import statArticlesByProvince from '@/views/stat/components/statArticlesByProvince.vue'
import statArticlesBySubject from '@/views/stat/components/statArticlesBySubject.vue'
import statArticlesByYear from '@/views/stat/components/statArticlesByYear.vue'
import statKwsByCount from '@/views/stat/components/statKwsByCount.vue'
import statPersonsByCoAuthor from '@/views/stat/components/statPersonsByCoAuthor.vue'
import statStyleByFund from '@/views/stat/components/statStyleByFund.vue'

import wordCloundForKeyWord from '@/views/stat/components/wordCloundForKeyWord.vue'

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
        path: '/file/index',
        name: '分析数据',
        component: FileIndex
      },
      {
        path: '/dataset/index',
        name: '数据显示',
        component: DatasetIndex
      },
      { path: '/to/showing/index', redirect: '/dataset/index' },
      {
        path: '/stat/index',
        name: '知识图谱',
        component: StatIndex,
        children: [
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
            path: '/coocMatrix/keyword/:dsid',
            name: '关键词共现矩阵',
            component: coocMatrixForKeyWord
          },
          {
            path: '/coocMatrix/topicword/:dsid',
            name: '主题词共现矩阵',
            component: coocMatrixForTopicWord
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
            path: '/stat/statArticlesByAuthor/:dsid',
            name: '作者发文量',
            component: statArticlesByAuthor
          },
          {
            path: '/stat/statArticlesByCountry/:dsid',
            name: '国家发文量',
            component: statArticlesByCountry
          },
          {
            path: '/stat/statArticlesByFirstDuty/:dsid',
            name: '一作发文量',
            component: statArticlesByFirstDuty
          },
          {
            path: '/stat/statArticlesByFund/:dsid',
            name: '基金支持发文量',
            component: statArticlesByFund
          },
          {
            path: '/stat/statArticlesByJournal/:dsid',
            name: '期刊来源统计',
            component: statArticlesByJournal
          },
          {
            path: '/stat/statArticlesByOrg/:dsid',
            name: '机构发文量',
            component: statArticlesByOrg
          },
          {
            path: '/stat/statArticlesByProvince/:dsid',
            name: '地区发文量',
            component: statArticlesByProvince
          },
          {
            path: '/stat/statArticlesByJournal/:dsid',
            name: '期刊发文量',
            component: statArticlesByJournal
          },
          {
            path: '/stat/statArticlesBySubject/:dsid',
            name: '学科分布统计',
            component: statArticlesBySubject
          },
          {
            path: '/stat/statArticlesByYear/:dsid',
            name: '历年发文量',
            component: statArticlesByYear
          },
          {
            path: '/stat/statKwsByCount/:dsid',
            name: '关键词词频',
            component: statKwsByCount
          },
          {
            path: '/stat/statPersonsByCoAuthor/:dsid',
            name: '合著人数统计',
            component: statPersonsByCoAuthor
          },
          {
            path: '/stat/statStyleByFund/:dsid',
            name: '基金类型统计',
            component: statStyleByFund
          },
          {
            path: '/wordclound/keyword/:dsid',
            name: '关键词词频',
            component: wordCloundForKeyWord
          }
        ]
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
