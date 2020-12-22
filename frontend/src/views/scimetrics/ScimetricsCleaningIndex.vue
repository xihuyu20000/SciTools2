<template>
  <el-container>
    <el-aside width="300px">
      <dataset-tree style="margin-top:20px"></dataset-tree>
    </el-aside>
    <el-main> <dataset-table></dataset-table></el-main>
  </el-container>
</template>

<script>
import DatasetTree from './components/DatasetTree.vue'
import DatasetTable from './components/DatasetTable.vue'

export default {
  data() {
    return {}
  },
  mounted() {},
  methods: {},
  components: { DatasetTree, DatasetTable }
}
</script>

<style lang="scss" scoped></style>
