import Vue from 'vue'
Vue.prototype.$api = {
  login: '/api/login',
  token: '/api/token',

  config: '/api/config/',
  config_save: '/api/config/save',

  dataset_upload: '/api/dataset/upload',
  dataset_list_names: '/api/dataset/list/names',
  dataset_list: '/api/dataset/list',
  dataset_clean: '/api/dataset/clean',
  dataset_delete: '/api/dataset/delete',
  dataset_rename: '/api/dataset/rename',
  dataset_show_process: '/api/dataset/show/process',
  datasete_odsbib_delete: '/api/dataset/odsbib/delete',
  datasete_odsbib_update: '/api/dataset/odsbib/update',

  advanced_upload: '/api/advanced/upload',
  advanced_tbls_list_names: '/api/advanced/tblnames',
  advanced_tbls_rename: '/api/advanced/tblrename',
  advanced_tbls_delete: '/api/advanced/delete',
  advanced_dataset_query: '/api/advanced/dataset_query',
  advanced_dataset_cleaning: '/api/advanced/dataset_cleaning',
  advanced_dataset_update: '/api/advanced/dataset_update',
  advanced_dataset_saveAsNew: '/api/advanced/dataset_saveAsNew',
  advanced_tbls_list_fieldconfigs: '/api/advanced/list_fieldconfigs',
  advanced_tbls_save_fieldconfigs: '/api/advanced/save_fieldconfigs',
  advanced_graphs_load_option_data: '/api/advanced/graph/load_option_data'
}
