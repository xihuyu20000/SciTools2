<template>
  <el-container>
    <el-aside width="300px">
      <graph-left-tree style="margin-top:20px;margin-bottom:20px"></graph-left-tree>
    </el-aside>
    <el-main> <graph-data-table></graph-data-table></el-main>
  </el-container>
</template>

<script>
import GraphLeftTree from './components/GraphLeftTree'
import GraphDataTable from './components/GraphDataTable'

export default {
  data() {
    return {}
  },
  mounted() {},
  methods: {},
  components: { GraphLeftTree, GraphDataTable }
}
</script>

<style lang="scss" scoped></style>
