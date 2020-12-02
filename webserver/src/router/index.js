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

import statArticlesByAuthor from '@/views/stat/graph/statArticlesByAuthor.vue'
import statArticlesByCountry from '@/views/stat/graph/statArticlesByCountry.vue'
import statArticlesByFirstDuty from '@/views/stat/graph/statArticlesByFirstDuty.vue'
import statArticlesByFund from '@/views/stat/graph/statArticlesByFund.vue'
import statArticlesByJournal from '@/views/stat/graph/statArticlesByJournal.vue'
import statArticlesByOrg from '@/views/stat/graph/statArticlesByOrg.vue'
import statArticlesByProvince from '@/views/stat/graph/statArticlesByProvince.vue'
import statArticlesBySubject from '@/views/stat/graph/statArticlesBySubject.vue'
import statArticlesByYear from '@/views/stat/graph/statArticlesByYear.vue'
import statKwsByCount from '@/views/stat/graph/statKwsByCount.vue'
import statPersonsByCoAuthor from '@/views/stat/graph/statPersonsByCoAuthor.vue'
import statStyleByFund from '@/views/stat/graph/statStyleByFund.vue'
import statTwsByCount from '@/views/stat/graph/statTwsByCount.vue'

import wordCloundForKeyWord from '@/views/stat/graph/wordCloundForKeyWord.vue'
import wordCloundForTopicWord from '@/views/stat/graph/wordCloundForTopicWord.vue'

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
            path: '/stat/statArticlesByAuthor',
            name: '作者发文量',
            component: statArticlesByAuthor
          },
          {
            path: '/stat/statArticlesByCountry',
            name: '国家发文量',
            component: statArticlesByCountry
          },
          {
            path: '/stat/statArticlesByFirstDuty',
            name: '一作发文量',
            component: statArticlesByFirstDuty
          },
          {
            path: '/stat/statArticlesByFund',
            name: '基金支持发文量',
            component: statArticlesByFund
          },
          {
            path: '/stat/statArticlesByJournal',
            name: '期刊来源统计',
            component: statArticlesByJournal
          },
          {
            path: '/stat/statArticlesByOrg',
            name: '机构发文量',
            component: statArticlesByOrg
          },
          {
            path: '/stat/statArticlesByProvince',
            name: '地区发文量',
            component: statArticlesByProvince
          },
          {
            path: '/stat/statArticlesBySubject',
            name: '学科分布统计',
            component: statArticlesBySubject
          },
          {
            path: '/stat/statArticlesByYear',
            name: '历年发文量',
            component: statArticlesByYear
          },
          {
            path: '/stat/statKwsByCount',
            name: '关键词词频',
            component: statKwsByCount
          },
          {
            path: '/stat/statPersonsByCoAuthor',
            name: '合著人数统计',
            component: statPersonsByCoAuthor
          },
          {
            path: '/stat/statStyleByFund',
            name: '基金类型统计',
            component: statStyleByFund
          },
          {
            path: '/stat/statTwsByCount',
            name: '主题词词频',
            component: statTwsByCount
          },
          {
            path: '/wordclound/keyword',
            name: '关键词词频',
            component: wordCloundForKeyWord
          },
          {
            path: '/wordclound/topicword',
            name: '主题词词频',
            component: wordCloundForTopicWord
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
