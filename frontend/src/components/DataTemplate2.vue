<template>
  <div>
    <common-table :globalConfig="globalConfig" :queryConfig="queryConfig" :tableConfig="tableConfig" ref="dataTable"> </common-table>
    <create-form :globalConfig="globalConfig" :formConfig="formConfig"></create-form>
  </div>
</template>

<script>
export default {
  props: {
    data: {
      type: Object,
      require: true
    }
  },
  data() {
    return {
      globalConfig: {},
      formConfig: [],
      queryConfig: [],
      tableConfig: [],
      editData: {}
    }
  },
  watch: {
    data: function(newVal) {
      this.globalConfig = newVal.data.globalConfig
      this.formConfig = newVal.data.formConfig
      this.queryConfig = newVal.data.queryConfig
      this.tableConfig = newVal.data.tableConfig
      this.$refs.dataTable.queryForm(this.globalConfig.url)
    }
  },
  methods: {
    relateRes: function(row) {
      console.log('关联用户', row)
    }
  },
  created() {}
}
</script>

<style lang="scss" scoped></style>
