<template>
  <div>
    <vxe-toolbar ref="xToolbar" :refresh="{ query: fetch }" print custom>
      <template v-slot:buttons>
        <vxe-button icon="fa fa-trash-o" status="perfect" @click="removeEvent">删除选中</vxe-button>
        <vxe-button icon="fa fa-save" status="perfect" @click="saveEvent">保存改动</vxe-button>
        <vxe-button icon="fa fa-mail-reply" status="perfect" @click="revertEvent">还原改动</vxe-button>
        <!--
        <vxe-button status="danger" :round="true" @click="showFilter" style="margin-left:50px;">数据过滤<i class="el-icon-caret-bottom" v-show="!isShowFilterBuilder"></i><i class="el-icon-caret-top" v-show="isShowFilterBuilder"></i></vxe-button>
        <vxe-button status="warning" :round="true" @click="saveDataset">另存为新数据集</vxe-button>
        -->
      </template>
    </vxe-toolbar>
    <div v-show="isShowFilterBuilder"><dataset-filter-builder></dataset-filter-builder></div>
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
      @edit-actived="editActivedEvent"
    >
      <vxe-table-column type="seq" width="60" fixed="left"></vxe-table-column>
      <vxe-table-column type="checkbox" width="60" fixed="left"></vxe-table-column>
      <vxe-table-column field="fileid" fixed="left"></vxe-table-column>
      <vxe-table-column field="id" fixed="left"></vxe-table-column>
      <vxe-table-column field="title" title="标题" min-width="300" fixed="left" sortable :edit-render="{ name: 'input', attrs: { type: 'text' } }" :filters="[{ label: '空值', value: '' }]"></vxe-table-column>
      <vxe-table-column field="firstduty" title="一作" min-width="150" sortable :edit-render="{ name: 'input', attrs: { type: 'text' } }" :filters="[{ label: '空值', value: '' }]"></vxe-table-column>
      <vxe-table-column field="pubyear" title="出版年" min-width="150" sortable :edit-render="{ name: 'input', attrs: { type: 'text' } }" :filters="[{ label: '空值', value: '' }]"></vxe-table-column>
      <vxe-table-column field="publication" title="出版物" min-width="250" sortable :edit-render="{ name: 'input', attrs: { type: 'text' } }" :filters="[{ label: '空值', value: '' }]"></vxe-table-column>
      <vxe-table-column field="authors" title="作者" min-width="250" sortable :edit-render="{ name: 'input', attrs: { type: 'text' } }" :filters="[{ label: '空值', value: '' }]"></vxe-table-column>
      <vxe-table-column field="orgs" title="机构" min-width="250" sortable :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="funds" title="基金" min-width="250" sortable :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="summary" title="摘要" min-width="100" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="style" title="类型" min-width="80" :edit-render="{ name: 'input', attrs: { type: 'text' } }"> </vxe-table-column>
      <vxe-table-column field="country" title="国别" min-width="80" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="lang" title="语种" min-width="80" :edit-render="{ name: 'input', attrs: { type: 'text' } }"></vxe-table-column>
      <vxe-table-column field="line" title="原始数据" min-width="400" :edit-render="{ name: 'input', attrs: { disabled: editDisabled } }"></vxe-table-column>
    </vxe-table>
  </div>
</template>

<script>
import DatasetFilterBuilder from './DatasetFilterBuilder.vue'
export default {
  components: { DatasetFilterBuilder },
  data() {
    return {
      dsid: '',
      loading: false,
      isShowFilterBuilder: false,
      editDisabled: true,
      tableData: []
    }
  },
  mounted() {
    this.$bus.$on(this.$api.dataset_list, dsid => {
      console.log('接收事件', dsid)
      this.dsid = dsid
      this.fetch()
    })
  },
  methods: {
    fetch() {
      this.loading = true
      return new Promise(resolve => {
        setTimeout(async () => {
          let _url = this.$api.dataset_list + '/' + this.dsid
          const { data: resp } = await this.$http.get(_url)
          //console.log('加载数据集', resp)
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
    editActivedEvent({ rowIndex, row }) {
      console.log('单元格编辑激活', rowIndex, row.title)
    },
    showFilter() {
      this.isShowFilterBuilder = !this.isShowFilterBuilder
    },
    removeEvent() {
      const selectRecords = this.$refs.xGrid.getCheckboxRecords()
      if (selectRecords.length) {
        this.$XModal.confirm('您确定要删除选中的数据吗?').then(async type => {
          if (type === 'confirm') {
            let dsidArr = selectRecords.map(row => {
              return row.id
            })
            let { data: resp } = await this.$http.post(this.$api.datasete_odsbib_delete, { ids: dsidArr })
            if (resp.status == 400) return this.$message.error(resp.msg)
            let newTableData = this.tableData.filter(v => {
              return !dsidArr.includes(v.id)
            })
            this.tableData = newTableData
            this.$refs.xGrid.removeCheckboxRow()
          }
        })
      } else {
        this.$XModal.message({ message: '请至少选择一条数据', status: 'error' })
      }
    },
    revertEvent() {
      this.$XModal.confirm('您确定要还原数据吗?').then(type => {
        if (type === 'confirm') {
          this.$refs.xGrid.revertData()
        }
      })
    },
    async saveEvent() {
      const { insertRecords, removeRecords, updateRecords } = this.$refs.xGrid.getRecordset()
      console.log(`insertRecords=${insertRecords.length} removeRecords=${removeRecords.length} updateRecords=${updateRecords.length}`)
      let { data: resp } = await this.$http.post(this.$api.datasete_odsbib_update, { datas: updateRecords })
      if (resp.status == 400) return this.$message.error(resp.msg)
      this.fetch()
    },
    saveDataset() {
      setTimeout(() => {
        const { fullData, visibleData, tableData, footerData } = this.$refs.xGrid.getTableData()
        console.log(fullData, visibleData, tableData, footerData)
      }, 100)
    },
    FilterPubyear({ value, row }) {
      console.log('过滤条件', value, row)
      return true
    },
    footerMethod({ columns, data }) {
      return [
        columns.map((column, columnIndex) => {
          if (columnIndex === 0) {
            return '空值'
          }
          if (['title', 'firstduty', 'pubyear', 'publication'].includes(column.property)) {
            let count = 0
            if (column.property == 'title') {
              count = 0
              data.forEach(ele => {
                if (ele.title.length == 0) count += 1
              })
            }
            if (column.property == 'firstduty') {
              count = 0
              data.forEach(ele => {
                if (ele.firstduty.length == 0) count += 1
              })
            }
            if (column.property == 'pubyear') {
              count = 0
              data.forEach(ele => {
                if (ele.pubyear.length == 0) count += 1
              })
            }
            if (column.property == 'publication') {
              count = 0
              data.forEach(ele => {
                if (ele.publication.length == 0) count += 1
              })
            }
            return count
          }
          return null
        })
      ]
    }
  }
}
</script>

<style></style>
