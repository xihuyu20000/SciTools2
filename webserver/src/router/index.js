import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/common/Home.vue'
import Default from '@/views/common/Default.vue'
import Login from '@/views/common/Login.vue'
import V404 from '@/views/common/404.vue'

import FileIndex from '@/views/file/FileIndex.vue'
import DatasetIndex from '@/views/dataset/DatasetIndex.vue'
import StatIndex from '@/views/stat/StatIndex.vue'
import statArticlesByYear from '@/views/stat/graph/statArticlesByYear.vue'
import statArticlesByCountry from '@/views/stat/graph/statArticlesByCountry.vue'
import ConfigIndex from '@/views/config/ConfigIndex.vue'

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
            path: '/stat/statArticlesByYear',
            name: '历年发文量',
            component: statArticlesByYear
          },
          {
            path: '/stat/statArticlesByCountry',
            name: '国家发文量',
            component: statArticlesByCountry
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
