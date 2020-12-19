<template>
  <div class="data-container">
    <div class="header">
      <div class="operate-bar">
        <el-button type="primary" @click="handleCreate">新增</el-button>
      </div>
      <div class="query-box">
        <el-form v-if="queryConfig.length > 0" :inline="true" :model="formModel">
          <el-form-item v-for="(config, index) in queryConfig" :key="index">
            <el-input v-if="config.style == 'textline'" v-model="formModel[config.field]" :placeholder="config.label"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" icon="el-icon-search" @click="queryForm(globalConfig.url)">查询</el-button>
          </el-form-item>
        </el-form>
        <div class="operator-bar">
          <slot name="header"></slot>
        </div>
      </div>
    </div>
    <div class="data-box">
      <el-table :data="tableData" row-key="id" border default-expand-all>
        <el-table-column type="selection" width="55"> </el-table-column>
        <template v-for="(config, index) in tableConfig">
          <el-table-column v-if="config.style === 'icon'" :key="index" :label="config.label" :prop="config.field" :width="config.width" :sortable="config.sortable">
            <template slot-scope="scope">
              <i :class="scope.row.icon"></i>
            </template>
          </el-table-column>
          <el-table-column v-else :key="index" :label="config.label" :prop="config.field" :width="config.width" :sortable="config.sortable"> </el-table-column>
        </template>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-popconfirm title="确定删除吗？" @onConfirm="handleDelete(scope.$index, scope.row)">
              <el-button type="danger" slot="reference">删除</el-button>
            </el-popconfirm>
            <slot name="row" :row="scope.row"></slot>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  props: ['config'],
  data() {
    return {
      globalConfig: { url: '' },
      queryConfig: [],
      tableConfig: [],
      formModel: {},
      tableData: []
    }
  },
  watch: {
    config: function(newVal) {
      this.globalConfig = newVal.globalConfig
      this.queryConfig = newVal.queryConfig
      this.tableConfig = newVal.tableConfig
      this.tableData = newVal.tableData
    }
  },
  methods: {
    async queryForm(url) {
      const { data: resp } = await this.$http(url + '?' + this.$ser(this.formModel))
      this.tableData = resp.data
    },
    async handleCreate() {
      this.$bus.$emit(this.$bus.showCreateDialog)
    },
    async handleEdit(index, row) {
      this.$bus.$emit(this.$bus.showEditDialog, row)
    },
    async handleDelete(index, row) {
      const { data: resp } = await this.$http.delete(this.globalConfig.url + '/' + row.id)
      console.log('删除', resp)
      if (resp.data == 1) {
        this.$message.success('删除成功')
        this.queryForm(this.globalConfig.url)
      } else {
        this.$message.error('删除失败')
      }
    }
  },
  mounted() {
    this.$bus.$on(this.$bus.loadData, () => {
      this.queryForm(this.globalConfig.url)
    })
  }
}
</script>

<style lang="scss" scoped>
.data-container {
  .header {
    display: flex;
    .operate-bar {
      margin-right: 20px;
    }
    .query-box {
      display: flex;
    }
  }
  .data-box {
  }
  .data-pager {
    margin-top: 10px;
  }
}
</style>
