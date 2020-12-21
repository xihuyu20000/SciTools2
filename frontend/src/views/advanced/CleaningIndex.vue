<template>
  <el-container>
    <el-aside width="300px">
      <cleaning-left-tree style="margin-top:20px;margin-bottom:20px"></cleaning-left-tree>
    </el-aside>
    <el-main> <cleaning-data-table></cleaning-data-table></el-main>
  </el-container>
</template>

<script>
import CleaningLeftTree from './components/CleaningLeftTree'
import CleaningDataTable from './components/CleaningDataTable'

export default {
  data() {
    return {}
  },
  mounted() {},
  methods: {},
  components: { CleaningLeftTree, CleaningDataTable }
}
</script>

<style lang="scss" scoped></style>
