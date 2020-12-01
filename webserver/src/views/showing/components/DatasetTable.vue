<template>
  <div>
    <vxe-grid border show-overflow show-header-overflow highlight-hover-row highlight-current-row ref="xGrid" height="600" :loading="loading" :toolbar-config="{ slots: { buttons: 'toolbar_buttons' } }" :checkbox-config="{ checkField: 'checked', labelField: 'nickname' }">
      <template v-slot:toolbar_buttons>
        <vxe-button @click="loadColumnAndData(10000, 10000)">1w列1w条</vxe-button>
        <vxe-button @click="loadColumnAndData(10000, 50000)">1w列5w条</vxe-button>
        <vxe-button @click="loadColumnAndData(10000, 100000)">1w列10w条</vxe-button>
        <vxe-button @click="loadColumnAndData(10000, 100000)">1w列20w条</vxe-button>
        <vxe-button @click="loadColumnAndData(20000, 50000)">2w列5w条</vxe-button>
        <vxe-button @click="loadColumnAndData(20000, 100000)">2w列10w条</vxe-button>
        <vxe-button @click="loadColumnAndData(20000, 200000)">2w列20w条</vxe-button>
        <vxe-button @click="$refs.xGrid.setAllCheckboxRow(true)">所有选中</vxe-button>
        <vxe-button @click="$refs.xGrid.clearCheckboxRow()">清除选中</vxe-button>
        <vxe-button @click="getSelectEvent">获取选中</vxe-button>
      </template>
    </vxe-grid>
  </div></template
>

<script>
import XEAjax from 'xe-ajax'
export default {
  data() {
    return {
      loading: false
    }
  },
  created() {
    this.loadColumnAndData(600, 600)
  },
  methods: {
    loadColumnAndData(colSize, rowSize) {
      this.loading = true
      Promise.all([XEAjax.mockColumns(colSize), XEAjax.mockList(rowSize)]).then(rest => {
        const columns = rest[0]
        const data = rest[1]
        const startTime = Date.now()
        const xGrid = this.$refs.xGrid
        // 使用函数式加载，阻断 vue 对大数组的双向绑定
        if (xGrid) {
          Promise.all([xGrid.reloadColumn(columns), xGrid.reloadData(data)]).then(() => {
            this.$XModal.message({ message: `渲染 ${colSize} 列 ${rowSize} 行，用时 ${Date.now() - startTime}毫秒`, status: 'info' })
            this.loading = false
          })
        }
      })
    },
    getSelectEvent() {
      let selectRecords = this.$refs.xGrid.getCheckboxRecords()
      this.$XModal.alert(selectRecords.length)
    }
  }
}
</script>

<style></style>
