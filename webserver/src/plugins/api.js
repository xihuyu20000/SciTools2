import Vue from 'vue'
Vue.prototype.$api = {
  login: '/api/login',
  file_upload: '/api/file/upload',
  config: '/api/config/',
  config_save: '/api/config/save',
  dataset_list_names: '/api/dataset/list/names',
  dataset_list: '/api/dataset/list'
}
