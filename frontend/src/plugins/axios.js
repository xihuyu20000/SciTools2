import Vue from 'vue'
import axios from 'axios'
axios.defaults.baseURL = 'http://localhost:8000'
axios.defaults.timeout = 30000

import NProgress from 'nprogress'
import 'nprogress/nprogress.css'

axios.interceptors.request.use(
  config => {
    NProgress.start()
    config.headers['Authorization'] = window.sessionStorage.getItem('token')
    return config
  },
  error => {
    console.log('axios.js报错', error) // for debug
    return Promise.reject(error)
  }
)

axios.interceptors.response.use(config => {
  NProgress.done()
  return config
})
Vue.prototype.$http = axios
