import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import common from '../components/common-vuex'
import material from '../views/teach/material/vuex-material'
export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: { common, material }
})
