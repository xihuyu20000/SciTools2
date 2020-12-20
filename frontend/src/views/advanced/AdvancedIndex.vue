<template>
  <el-container>
    <el-aside width="300px">
      <advanced-left-tree style="margin-top:20px;margin-bottom:20px"></advanced-left-tree>
    </el-aside>
    <el-main> <advanced-data-table></advanced-data-table></el-main>
  </el-container>
</template>

<script>
import AdvancedLeftTree from './components/AdvancedLeftTree'
import AdvancedDataTable from './components/AdvancedDataTable'

export default {
  data() {
    return {}
  },
  mounted() {},
  methods: {},
  components: { AdvancedLeftTree, AdvancedDataTable }
}
</script>

<style lang="scss" scoped></style>
