<template>
  <div>
    <vxe-toolbar ref="xToolbar" :refresh="{ query: fetch }" print custom>
      <template v-slot:buttons>
        <vxe-button @click="filterDataset">数据筛选</vxe-button>
        <vxe-button @click="toFieldConfig">字段设置</vxe-button>
        <vxe-button @click="showProcessing">显示进度</vxe-button>
      </template>
    </vxe-toolbar>
    <!-- <div v-show="isShowFilterBuilder"><dataset-filter-builder></dataset-filter-builder></div> -->
    <vxe-grid
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
      :mouse-config="{ selected: true }"
      :edit-config="{ trigger: 'dblclick', mode: 'cell', showStatus: true }"
      :keyboard-config="{ isArrow: true }"
      :footer-method="footerMethod"
      :customs="[
        { field: 'fileid', visible: false },
        { field: 'id', visible: false }
      ]"
      :columns.sync="titles"
      :data.sync="dataset"
      @cell-dblclick="dbclickCell"
      @edit-closed="editClosedEvent"
      @edit-actived="editActivedEvent"
    >
    </vxe-grid>
    <cleaning-data-filter :titles="titles" :dataset="dataset"></cleaning-data-filter>
    <cleaning-field-config></cleaning-field-config>
  </div>
</template>

<script>
import CleaningDataFilter from './CleaningDataFilter.vue'
import CleaningFieldConfig from './CleaningFieldConfig.vue'
export default {
  components: { CleaningDataFilter, CleaningFieldConfig },
  data() {
    return {
      ad_tbl: '',
      loading: false,
      editDisabled: true,
      titles: [],
      dataset: []
    }
  },
  mounted() {
    this.$bus.$on(this.$api.advanced_dataset_query, ad_tbl => {
      // console.log('接收事件', ad_tbl)
      this.ad_tbl = ad_tbl
      this.fetch()
    })
    this.$bus.$on('advanced_reload_dataset', () => this.fetch())
  },
  methods: {
    async fetch() {
      this.loading = true

      let _url = this.$api.advanced_dataset_query + '/' + this.ad_tbl.tblid
      const { data: resp } = await this.$http.get(_url)
      if (resp.status == 400) return this.$message.error(resp.msg)

      let titles = resp.data[0]
      let dataset = resp.data[1]
      this.titles = titles.map(item => {
        return item
      })
      this.dataset = dataset.map(item => {
        return item
      })
      if (this.$refs.xGrid) {
        this.$refs.xGrid.reloadColumn(this.titles)
        this.$refs.xGrid.reloadData(this.dataset)
      }
      //console.log('表头信息', this.titles)
      //console.log('数据信息', this.dataset)
      this.loading = false
    },
    dbclickCell({ row, column }) {
      console.log('单元格', row, column)
    },
    editActivedEvent({ rowIndex, row }) {
      console.log('单元格编辑激活', rowIndex, row.title)
    },
    filterDataset() {
      // 数据筛选
      if (this.ad_tbl == '') return this.$message.error('请选择数据集')
      this.$bus.$emit('show_cleaning_data_filter', this.ad_tbl)
    },
    toFieldConfig() {
      // 字段设置
      if (this.ad_tbl == '') return this.$message.error('请选择数据集')
      this.$bus.$emit('show_cleaning_data_fileconfig', this.ad_tbl)
    },
    showProcessing() {
      this.$bus.$emit('showWebSocketMsg', '执行进度')
    },
    editClosedEvent({ row, column }) {
      let xGrid = this.$refs.xGrid
      let field = column.property
      let cellValue = row[field]
      let id = row['id']
      // 判断单元格值是否被修改
      if (xGrid.isUpdateByRow(row, field)) {
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
    footerMethod({ columns, data }) {
      data
      return [
        columns.map((column, columnIndex) => {
          if (columnIndex === 0) {
            return '空值'
          }
          return null
        })
      ]
    }
  }
}
</script>

<style lang="scss" scoped></style>
