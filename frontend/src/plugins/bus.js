import Vue from 'vue'
const v = new Vue()
v.loadData = 'e_load_data'
v.showCreateDialog = 'e_show_create_dialog'
v.showEditDialog = 'e_show_edit_dialog'
v.loadDataset = 'e_load_dataset'
Vue.prototype.$bus = v
