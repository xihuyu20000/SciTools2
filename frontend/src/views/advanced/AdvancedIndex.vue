<template>
  <el-container>
    <el-aside width="300px">
      <advanced-data-tree style="margin-top:20px;margin-bottom:20px"></advanced-data-tree>
    </el-aside>
    <el-main> <advanced-data-table></advanced-data-table></el-main>
  </el-container>
</template>

<script>
import AdvancedDataTree from './components/AdvancedDataTree'
import AdvancedDataTable from './components/AdvancedDataTable'

export default {
  data() {
    return {}
  },
  mounted() {},
  methods: {},
  components: { AdvancedDataTree, AdvancedDataTable }
}
</script>

<style lang="scss" scoped></style>
