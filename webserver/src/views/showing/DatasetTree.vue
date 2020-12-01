<template>
  <div class="jstree" ref="app"></div>
</template>

<script>
import $ from 'jquery'
export default {
  data() {
    return {
      node: {},
      tableData: []
    }
  },
  mounted() {
    $('.jstree')
      .jstree({
        core: {
          data: [
            {
              id: '0',
              parent: '#',
              state: { disabled: false, opened: true, selected: false },
              text: '张三档案'
            },
            { id: '1', parent: '#', text: '李四档案' },
            { id: '2', parent: '#', text: '王五档案' },
            { id: '3', parent: '#', text: '李六档案' },
            { id: '4', parent: '#', text: '陈七档案' },
            { id: '41', parent: '4', text: '踩踩踩' }
          ],
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
    // 选中项上移
    //moveup() {
    //  var ref = $("#app").jstree(true);
    //  var currNode = this._getCurrNode();
    //  var prevNode = ref.get_prev_dom(currNode, true);
    //  ref.move_node(currNode, prevNode, "before");
    //},
    // 选中项下移
    //movedown() {
    //  var ref = $("#app").jstree(true);
    //  var currNode = this._getCurrNode();
    //  var nextNode = ref.get_next_dom(currNode, true); //返回兄弟节点的下一个节点
    //  ref.move_node(currNode, nextNode, "after");
    //},
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
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  border: 1px solid red;
}
.main {
  width: 100%;
}
</style>
