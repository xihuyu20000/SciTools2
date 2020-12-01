<template>
  <div class="jstree" ref="app"></div>
</template>

<script>
import $ from 'jquery'
export default {
  data() {
    return {
      dataarr: []
    }
  },
  mounted() {
    this.fetch()

    $.contextMenu({
      selector: '#app', //覆盖原来的右键选择器，并指定作用范围
      callback: (key, options) => {
        console.log(key, options) // 是下面items中的键：add/rename/del
        switch (key) {
          case 'rename':
            this.rename()
            break
          case 'del':
            this.del()
            break
          default:
            break
        }
      },
      items: {
        //菜单列表配置
        rename: { name: '重命名' },
        del: { name: '删除' }
      }
    })
  },
  methods: {
    async fetch() {
      const { data: resp } = await this.$http.get(this.$api.listFiles)
      if (resp.status == 400) return this.$message.error(resp.msg)
      this.dataarr = resp.data.map(item => {
        let json = {}
        json.id = item.fileid
        json.parent = '#'
        json.text = item.filename
        return json
      })
      this.loadjstree()
    },
    loadjstree() {
      $('.jstree')
        .jstree({
          core: {
            data: this.dataarr,
            themes: {
              variant: 'large', //加大
              ellipsis: true //文字多时省略
            },
            check_callback: true
          },
          plugins: ['wholerow', 'themes']
        })
        .on('select_node.jstree', (event, data) => {
          this.node = data.node // 获取选中的项，并保存在data数据中
        })
        .on('changed.jstree', (event, data) => {
          this.node = data.node
        })
    },
    // 重命名新节点
    rename() {
      var ref = $('#app').jstree(true)
      var currNode = this._getCurrNode()
      let text = this.node.text // 暂存需要重名名节点的原始text
      ref.rename_node(currNode) // 重命名节点
      if (currNode) {
        ref.edit(currNode, text) // 让重命名的节点处于编辑状态
      }
    },
    // 删除选中的节点
    del() {
      var ref = $('#app').jstree(true)
      var currNode = this._getCurrNode()
      ref.delete_node(currNode)
    },
    _getCurrNode() {
      var ref = $('#app').jstree(true),
        sel = ref.get_selected()
      console.log(sel)
      if (!sel.length) {
        // 若没有选中，则返回false
        return false
      }
      sel = sel[0]
      return sel // 把选中的第一个项的 id 返回
    }
  },
  components: {}
}
</script>

<style lang="scss" scoped>
.jstree {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 20px;
  border: 1px solid gray;
}
.main {
  width: 100%;
}
</style>
