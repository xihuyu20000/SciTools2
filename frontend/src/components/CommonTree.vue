<template>
  <el-tree :data="data" :props="defaultProps" node-key="id" default-expand-all @node-click="handleNodeClick" :render-content="renderContent"></el-tree>
</template>

<script>
export default {
  props: {
    globalConfig: {
      type: Object,
      required: true,
      default: function() {
        return { url: '' }
      }
    }
  },
  data() {
    return {
      data: [],
      defaultProps: {
        children: 'children',
        label: 'label'
      }
    }
  },
  methods: {
    async loadData(url) {
      const { data: resp } = await this.$http.get(url + '/tree')
      this.data = resp.data
    },
    async handleNodeClick(data) {
      if (data.style != '角色') return false
      let _url = this.globalConfig.url + '/user/' + data.id
      console.log('蓝线节点', _url)
      const { data: resp } = await this.$http.get(_url)
      console.log(resp)
    },
    renderContent(h, { node, data }) {
      return data.style == '角色' ? (
        <span>
          <i class="el-icon-s-opportunity"></i>
          <font color="#409EFF">{node.label}</font>
        </span>
      ) : (
        <span>{node.label}</span>
      )
    }
  }
}
</script>

<style lang="scss" scoped></style>
