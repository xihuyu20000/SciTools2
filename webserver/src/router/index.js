import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/common/Home.vue'
import Default from '@/views/common/Default.vue'
import Login from '@/views/common/Login.vue'
import V404 from '@/views/common/404.vue'
import IndexUser from '@/views/sys/IndexUser.vue'
import TemplateLoader from '@/views/common/TemplateLoader.vue'

import DataFileList from '@/views/da/datafile/DataFileList.vue'
import DataSetList from '@/views/da/dataset/DataSetList.vue'

import EchartsLine from '@/views/graph/line/EchartsLine.vue'

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
        path: '/dt/:id/index',
        name: '加载模板',
        component: TemplateLoader
      },
      {
        path: '/sys/user/index',
        name: '用户列表',
        component: IndexUser
      },
      {
        path: '/da/datafile/list',
        name: '数据文件列表',
        component: DataFileList
      },
      {
        path: '/da/dataset/list',
        name: '数据集列表',
        component: DataSetList
      },
      {
        path: '/graph/line/echartsLine',
        name: '折线图',
        component: EchartsLine
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

router.beforeEach((to, from, next) => {
  // console.log("from", from);
  // 获取token
  const token = sessionStorage.getItem('token')
  // 如果是登录或者有token，则通过
  if (to.path === '/login' || token) return next()
  console.error('未授权用户，请登录')
  next('/login')
})

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

export default router
