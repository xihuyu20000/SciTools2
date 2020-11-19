module.exports = {
  namespaced: true,
  state: { menuTree: [] },
  getters: {
    headerNav: function(state) {
      state.menuTree = JSON.parse(localStorage.getItem('menuTree'))
      return state.menuTree.filter(item => item.pid == 0)
    }
  },
  mutations: {
    // setMenuTree: function(state, data) {
    //   state.menuTree = data;
    // }
  },
  actions: {},
  modules: {}
}
