import Vue from 'vue'
Vue.prototype.$api = {
  login: '/api/login',
  // navs: '/api/navs',
  upload: '/api/file/upload',
  configIndex: '/api/config/',
  configSave: '/api/config/save',
  listDataset: '/api/stat/list_dataset',
  listFiles: '/api/stat/list_files'
}
