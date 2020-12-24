<template>
  <div>
    <vxe-toolbar ref="xToolbar" :refresh="{ query: fetch }" print custom>
      <template v-slot:buttons>
        <vxe-button @click="filterDataset">数据筛选</vxe-button>
        <vxe-button @click="toFieldConfig">字段设置</vxe-button>
        <vxe-button @click="filterDataset">数据合并</vxe-button>
        <vxe-button @click="filterDataset">生成图表</vxe-button>
      </template>
    </vxe-toolbar>
    <!-- <div v-show="isShowFilterBuilder"><dataset-filter-builder></dataset-filter-builder></div> -->
    <vxe-table
      ref="xGrid"
      border
      resizable
      keep-source
      show-footer
      show-overflow
      show-header-overflow
      highlight-current-row
      highlight-hover-row
      type="seq"
      max-height="500px"
      :print-config="{}"
      :loading="loading"
      :data="tableData"
      :mouse-config="{ selected: true }"
      :edit-config="{ trigger: 'dblclick', mode: 'cell', showStatus: true }"
      :keyboard-config="{ isArrow: true }"
      :footer-method="footerMethod"
      :customs="[
        { field: 'fileid', visible: false },
        { field: 'id', visible: false }
      ]"
      @cell-dblclick="dbclickCell"
      @edit-closed="editClosedEvent"
      @edit-actived="editActivedEvent"
    >
    </vxe-table>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      ad_tbl: '',
      loading: false,
      editDisabled: true,
      tableData: []
    }
  },
  mounted() {
    this.$bus.$on(this.$api.advanced_dataset_query, ad_tbl => {
      // console.log('接收事件', ad_tbl)
      this.ad_tbl = ad_tbl
      this.fetch()
    })
  },
  methods: {
    async fetch() {
      this.loading = true

      let _url = this.$api.advanced_dataset_query + '/' + this.ad_tbl.tblid
      const { data: resp } = await this.$http.get(_url)
      let titles = resp.data[0]
      let dataset = resp.data[1]
      titles = titles.map(item => {
        return item
      })
      dataset = dataset.map(item => {
        return item
      })
      this.$refs.xGrid.reloadColumn(titles)
      this.$refs.xGrid.reloadData(dataset)
      console.log('加载数据集', resp)
      if (resp.status == 400) return this.$message.error(resp.msg)
      // this.tableData = resp.data
      this.loading = false
    },
    dbclickCell({ row, column }) {
      console.log('单元格', row, column)
    },
    editActivedEvent({ rowIndex, row }) {
      console.log('单元格编辑激活', rowIndex, row.title)
    },

    filterDataset() {
      // 高级过滤
      return this.$message.error('正在开发中.....')
    },
    toFieldConfig() {
      this.$router.push('/advanced/fieldconfig/' + this.ad_tbl.tblid)
    },
    editClosedEvent({ row, column }) {
      let xTable = this.$refs.xGrid
      let field = column.property
      let cellValue = row[field]
      let id = row['id']
      // 判断单元格值是否被修改
      if (xTable.isUpdateByRow(row, field)) {
        // console.log('实时保存', field, cellValue, id)
        setTimeout(async () => {
          let { data: resp } = await this.$http.post(this.$api.datasete_odsbib_update, { id: id, k: field, v: cellValue })
          if (resp.status == 400) return this.$message.error(resp.msg)
          this.$XModal.message({
            message: `保存成功！`,
            status: 'success'
          })
          // 局部更新单元格为已保存状态
          this.$refs.xGrid.reloadRow(row, null, field)
        }, 300)
      }
    },
    FilterPubyear({ value, row }) {
      console.log('过滤条件', value, row)
      return true
    },
    footerMethod({ columns, data }) {
      console.log(data)
      return [
        columns.map((column, columnIndex) => {
          if (columnIndex === 0) {
            return '空值'
          }
          // if (['title', 'firstduty', 'pubyear', 'publication'].includes(column.property)) {
          //   let count = 0
          //   if (column.property == 'title') {
          //     count = 0
          //     data.forEach(ele => {
          //       if (ele.title.length == 0) count += 1
          //     })
          //   }
          //   if (column.property == 'firstduty') {
          //     count = 0
          //     data.forEach(ele => {
          //       if (ele.firstduty.length == 0) count += 1
          //     })
          //   }
          //   if (column.property == 'pubyear') {
          //     count = 0
          //     data.forEach(ele => {
          //       if (ele.pubyear.length == 0) count += 1
          //     })
          //   }
          //   if (column.property == 'publication') {
          //     count = 0
          //     data.forEach(ele => {
          //       if (ele.publication.length == 0) count += 1
          //     })
          //   }
          //   return count
          // }
          return null
        })
      ]
    }
  }
}
</script>

<style></style>
