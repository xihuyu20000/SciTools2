<template>
  <el-container>
    <el-aside width="300px">
      <scimetrics-dataset-tree style="margin-top:20px"></scimetrics-dataset-tree>
    </el-aside>
    <el-main> <scimetrics-dataset-table></scimetrics-dataset-table></el-main>
  </el-container>
</template>

<script>
import ScimetricsDatasetTree from './components/ScimetricsDatasetTree.vue'
import ScimetricsDatasetTable from './components/ScimetricsDatasetTable.vue'

export default {
  data() {
    return {}
  },
  mounted() {},
  methods: {},
  components: { ScimetricsDatasetTree, ScimetricsDatasetTable }
}
</script>

<style lang="scss" scoped></style>
