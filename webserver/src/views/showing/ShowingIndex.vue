<template>
  <el-container>
    <el-aside width="200px">
      <dataset-tree></dataset-tree>
    </el-aside>
    <el-main> <dataset-table></dataset-table></el-main>
  </el-container>
</template>

<script>
import DatasetTree from './DatasetTree'
import DatasetTable from './DatasetTable'
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
