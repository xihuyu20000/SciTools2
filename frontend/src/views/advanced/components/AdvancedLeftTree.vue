<template>
  <div>
    <el-tabs>
      <el-tab-pane label="数据集" name="first">
        <vue-tree-list @click="onClick" @change-name="onChangeName" @delete-node="onDel" :model="treeData">
          <template v-slot:leafNameDisplay="slotProps">
            <span class="icon">
              {{ slotProps.model.name }}
            </span>
          </template>
        </vue-tree-list>
      </el-tab-pane>
      <el-tab-pane label="图表集" name="second">配置管理</el-tab-pane>
    </el-tabs>

    <div><el-button type="info" style="margin-top:50px" @click="to_add_datasource">添加外部数据</el-button></div>
  </div>
</template>

<script>
import { VueTreeList, Tree, TreeNode } from 'vue-tree-list'
export default {
  components: {
    VueTreeList
  },
  data() {
    return {
      treeData: new Tree([])
    }
  },
  computed: {},
  mounted() {
    this.fetch()
  },
  methods: {
    to_add_datasource() {
      this.$router.push('/advanced/datasource')
    },
    async fetch() {
      let _url = this.$api.advanced_tbls_list_names
      const { data: resp } = await this.$http.get(_url)

      if (resp.status == 400) return this.$message.error(resp.msg)
      let top = resp.data
        .filter(function(v) {
          return v.pid == '' ? true : false
        })
        .map(function(v) {
          return {
            name: v.tblname,
            id: v.tblid,
            data: v, // 自定义属性，保存数据
            dragDisabled: true,
            addTreeNodeDisabled: true,
            addLeafNodeDisabled: true,
            editNodeDisabled: false,
            delNodeDisabled: false
          }
        })
      let _this = this
      top.forEach(function(item) {
        _this.treeData.addChildren(new TreeNode(item))
      })
    },
    onDel(node) {
      // 删除树节点
      this.$confirm('此操作将永久删除该数据集, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(async () => {
        let _url = this.$api.advanced_tbls_delete + '/' + node.id
        const { data: resp } = await this.$http.get(_url)
        if (resp.status == 400) return this.$message.error(resp.msg)
        node.remove()
        this.$bus.$emit(this.$api.dataset_list, '1')
      })
    },

    async onChangeName(node) {
      // 修改节点名称
      let _url = this.$api.advanced_tbls_rename + '/' + node.id + '/' + node.newName
      const { data: resp } = await this.$http.get(_url)
      if (resp.status == 400) return this.$message.error(resp.msg)
    },

    onClick(params) {
      // 点击树节点
      this.$bus.$emit(this.$api.advanced_dataset_query, params.data)
    }
  }
}
</script>

<style lang="scss" scoped>
.icon {
  cursor: pointer;
  padding: 0px;
}
div.vtl-tree-margin {
  margin-left: 0.5em;
}
</style>
