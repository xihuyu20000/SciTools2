<template>
  <el-container>
    <el-aside width="300px">
      <dataset-tree></dataset-tree>
    </el-aside>
    <el-main> <dataset-table></dataset-table></el-main>
  </el-container>
</template>

<script>
import DatasetTree from './components/DatasetTree'
import DatasetTable from './components/DatasetTable'

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
