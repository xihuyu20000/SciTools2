<template>
  <div>
    <common-table :config="config" ref="dataTable"> </common-table>
    <create-form :config="config"></create-form>
  </div>
</template>

<script>
export default {
  props: ['data'],
  data() {
    return {
      config: {}
    }
  },
  watch: {
    data: function(newVal) {
      this.config = newVal.data
      this.$refs.dataTable.queryForm(this.config.globalConfig.url)
    }
  }
}
</script>

<style lang="scss" scoped></style>
