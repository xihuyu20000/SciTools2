import Vue from 'vue'
Vue.prototype.$api = {
  login: '/api/login',
  file_upload: '/api/file/upload',
  config: '/api/config/',
  config_save: '/api/config/save',
  dataset_list_names: '/api/dataset/list/names',
  dataset_list: '/api/dataset/list',
  dataset_delete: '/api/dataset/delete',
  dataset_rename: '/api/dataset/rename',
  datasete_odsbib_delete: '/api/dataset/odsbib/delete',
  datasete_odsbib_update: '/api/dataset/odsbib/update'
}
