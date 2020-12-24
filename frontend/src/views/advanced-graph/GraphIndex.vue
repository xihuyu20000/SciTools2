<template>
  <el-container>
    <el-aside width="300px">
      <graph-left-tree style="margin-top:20px;margin-bottom:20px"></graph-left-tree>
    </el-aside>
    <el-main> <graph-design></graph-design></el-main>
  </el-container>
</template>

<script>
import GraphLeftTree from './components/GraphLeftTree.vue'
import GraphDesign from './components/GraphDesign.vue'

export default {
  data() {
    return {}
  },
  mounted() {},
  methods: {},
  components: { GraphLeftTree, GraphDesign }
}
</script>

<style lang="scss" scoped></style>
