<template>
  <div>
    <el-button-group>
      <el-button type="primary" size="medium" :icon="this.$store.state.material.treeExpandable ? 'el-icon-arrow-left' : 'el-icon-arrow-right'" @click="toggleTree" style="width:50px"></el-button>
      <el-tooltip class="item" effect="dark" content="添加下级" placement="right">
        <el-button type="primary" size="medium" style="width:50px" @click="formDialog = true">+</el-button>
      </el-tooltip>
    </el-button-group>
    <el-tree :data="treedata" node-key="id" default-expand-all :draggable="true" :expand-on-click-node="false" @node-click="clickTreeLeaf">
      <span class="tree-node-span" slot-scope="{ node, data }">
        <span>{{ node.label }}</span>
        <span>
          <el-button type="text" size="mini" @click="() => toedit(node, data)">
            修改
          </el-button>
          <el-button type="text" size="mini" @click="() => toremove(node, data)">
            删除
          </el-button>
          <el-button type="text" size="mini" @click="() => toappend(node, data)">
            添加下级
          </el-button>
        </span>
      </span>
    </el-tree>
    <el-dialog :title="title + '目录'" :visible="formDialog" @open="openDialog" @close="closeDialog">
      <el-form :model="formData" ref="form1">
        <el-form-item label="名称">
          <el-input v-model="formData.label"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="closeDialog">取 消</el-button>
        <el-button type="primary" @click="saveDialog">保 存</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formDialog: false,
      treedata: [],
      title: '创建',
      formData: {},
      rules: [{ label: [{ required: true, message: '名称', trigger: 'blur' }] }]
    }
  },
  methods: {
    toggleTree() {
      this.$store.commit('material/expandTree')
    },
    async clickTreeLeaf(data, node) {
      if (node.isLeaf) {
        console.log('叶子数据', data)
        console.log('叶子节点', node)
        this.$store.commit('material/setLeftNode', node)
        const { data: resp } = await this.$http.get('/material/category/' + data.id)
        this.$store.commit('material/setMaterial', resp.data)
      }
    },
    toedit: function(node, data) {
      this.title = '修改'
      this.formDialog = true
      this.formData = Object.assign({}, data)
    },
    toremove: async function(node, data) {
      const { data: resp } = await this.$http.delete('/material_category/' + data.id)
      if (resp.status != 200) return this.$message.error('删除失败')
      this.$message.success('删除成功')
      this.fetch()
    },
    toappend: function(node, data) {
      this.title = '添加下级'
      this.formDialog = true
      this.formData = Object.assign({}, { pid: data.id })
    },
    onMouseoverEnvDelBtn: function(event) {
      event.target.parentElement.querySelector('.env-del-btn-span').style.cssText += 'display:block'
    },
    onMouseleaveEnvDelBtn: function(event) {
      event.target.parentElement.querySelector('.env-del-btn-span').style.cssText += 'display:none'
    },
    openDialog: function() {},
    closeDialog: function() {
      this.formDialog = false
    },
    saveDialog: async function() {
      let result = {}
      if (this.title == '修改') {
        result = await this.$http.put('/material_category/' + this.formData.id, this.formData)
      } else {
        result = await this.$http.post('/material_category', this.formData)
      }
      if (result.data.status != 200) return this.$message.error('保存失败')
      this.$message.success('保存成功')
      this.formDialog = false
      this.fetch()
    },
    fetch: async function() {
      const { data: resp } = await this.$http.get('/material_category')
      this.treedata = JSON.parse(JSON.stringify(resp.data))
      console.log('分类', resp)
    }
  },
  created() {
    this.fetch()
  }
}
</script>

<style lang="scss" scoped>
.el-tree-node {
  height: 50px;
}
.tree-node-span {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 12px;
  .node-bar {
    margin-left: 20px;
  }
}
</style>
