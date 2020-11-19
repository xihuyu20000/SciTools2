<template>
  <el-container>
    <el-aside :width="this.$store.state.material.treeExpandable ? '400px' : '50px'">
      <comp-category-tree></comp-category-tree>
    </el-aside>
    <el-main>
      <comp-mark-down></comp-mark-down>
    </el-main>
  </el-container>
</template>

<script>
import CompCategoryTree from './CompCategoryTree'
import CompMarkDown from './CompMarkDown'
export default {
  data() {
    return {}
  },
  watch: {},

  components: { CompCategoryTree, CompMarkDown }
}
</script>

<style lang="scss" scoped>
.el-aside {
  margin-right: 10px;
}

.el-main {
  padding: 0;
}
</style>
