module.exports = {
  namespaced: true,
  state: { treeExpandable: true, leafNode: null, material: {} },
  getters: {},
  mutations: {
    expandTree: function(state) {
      state.treeExpandable = !state.treeExpandable
    },
    setLeftNode: function(state, node) {
      state.leafNode = node
    },
    setMaterial: function(state, data) {
      state.material = data
    }
  },
  actions: {}
}
