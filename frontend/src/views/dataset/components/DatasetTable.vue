<template>
  <div>
    <vxe-toolbar ref="xToolbar" :refresh="{ query: fetch }" export print custom>
      <template v-slot:buttons>
        <vxe-button status="danger" :round="true" @click="showFilter">数据过滤</vxe-button>
        <vxe-button :round="true" @click="saveDataset">另存为</vxe-button>
      </template>
    </vxe-toolbar>
    <el-card class="box-card">
      <el-row>
        <el-col :span="4">
          <el-select clearable placeholder="请选择字段">
            <el-option v-for="item in 10" :key="item" :label="item" :value="item"> </el-option>
          </el-select>
          <el-select clearable placeholder="请选择函数">
            <el-option v-for="item in 10" :key="item" :label="item" :value="item"> </el-option>
          </el-select>
        </el-col>
        <el-col :span="18"><el-input type="textarea" :rows="4" placeholder="请输入内容"> </el-input></el-col>
        <el-col :span="2">
          <el-link type="success">语法检查</el-link>
          <el-button>执行过滤</el-button>
        </el-col>
      </el-row>
    </el-card>
    <vxe-table
      ref="xGrid"
      border
      resizable
      show-overflow
      highlight-current-row
      show-header-overflow
      highlight-hover-row
      type="seq"
      max-height="500px"
      :print-config="{}"
      :loading="loading"
      :data="tableData"
      :mouse-config="{ selected: true }"
      :edit-config="{ trigger: 'dblclick', mode: 'cell', showStatus: true }"
      :keyboard-config="{ isArrow: true }"
      :customs="[
        { field: 'fileid', visible: false },
        { field: 'id', visible: false }
      ]"
      @cell-dblclick="dbclickCell"
    >
      <vxe-table-column type="seq" width="60"></vxe-table-column>
      <vxe-table-column type="checkbox" width="60"></vxe-table-column>
      <vxe-table-column field="fileid"></vxe-table-column>
      <vxe-table-column field="id"></vxe-table-column>
      <vxe-table-column field="style" title="类型" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="country" title="国别" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="lang" title="语种" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="title" title="标题" :edit-render="{ name: 'input', attrs: { type: 'text' } }" sortable></vxe-table-column>
      <vxe-table-column field="firstduty" title="第一责任人" :edit-render="{ name: 'input', attrs: { type: 'text' } }" sortable></vxe-table-column>
      <vxe-table-column field="pubyear" title="出版年" :edit-render="{ name: 'input', attrs: { type: 'text' } }" sortable></vxe-table-column>
      <vxe-table-column field="summary" title="摘要" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
    </vxe-table>
    共有条{{ tableData.length }}数据
  </div></template
>

<script>
export default {
  data() {
    return {
      loading: false,
      tableData: []
    }
  },
  mounted() {
    this.fetch()
  },
  methods: {
    fetch() {
      this.loading = true
      return new Promise(resolve => {
        setTimeout(async () => {
          const { data: resp } = await this.$http.get(this.$api.dataset_list + '/a1738a9d2b1511eb9066e8b1fca4ff37')
          if (resp.status == 400) return this.$message.error(resp.msg)
          this.tableData = resp.data
          this.loading = false
          resolve()
        }, 300)
      })
    },
    dbclickCell({ row, column }) {
      console.log('单元格', row, column)
    },
    showFilter() {},
    saveDataset() {
      setTimeout(() => {
        const { fullData, visibleData, tableData, footerData } = this.$refs.xGrid.getTableData()
        console.log(fullData, visibleData, tableData, footerData)
      }, 100)
    }
  }
}
</script>

<style></style>
