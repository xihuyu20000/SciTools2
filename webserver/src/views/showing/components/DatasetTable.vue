<template>
  <div>
    <vxe-toolbar ref="xToolbar" :refresh="{ query: fetch }" export print custom> </vxe-toolbar>
    <vxe-table
      ref="xGrid"
      border
      resizable
      show-overflow
      highlight-current-row
      show-header-overflow
      highlight-hover-row
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
      <vxe-table-column field="fileid"></vxe-table-column>
      <vxe-table-column field="id"></vxe-table-column>
      <vxe-table-column field="style" title="类型" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="country" title="国别" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="lang" title="语种" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="title" title="标题" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="firstduty" title="第一责任人" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="pubyear" title="出版年" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="summary" title="摘要" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
    </vxe-table></div
></template>

<script>
export default {
  data() {
    return {
      loading: false,
      tableData: []
    }
  },
  mounted() {
    this.$nextTick(() => {
      // 手动将表格和工具栏进行关联
      this.$refs.xGrid.connect(this.$refs.xToolbar)
    })
    this.fetch()
  },
  methods: {
    fetch() {
      this.loading = true
      return new Promise(resolve => {
        setTimeout(async () => {
          const { data: resp } = await this.$http.get(this.$api.listDataset)
          if (resp.status == 400) return this.$message.error(resp.msg)
          this.tableData = resp.data
          this.loading = false
          resolve()
        }, 300)
      })
    },
    dbclickCell({ row, column }) {
      console.log('单元格', row, column)
    }
  }
}
</script>

<style></style>
