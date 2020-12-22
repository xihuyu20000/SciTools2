<template>
  <el-container>
    <el-aside width="70px">
      <el-menu router :collapse="true" :default-active="activeMenu" style="height:100vh">
        <el-menu-item index="/scimetrics/datasource/index">
          <i class="el-icon-upload"></i>
          <span slot="title">数据源</span>
        </el-menu-item>
        <el-menu-item index="/scimetrics/cleaning/index">
          <i class="el-icon-loading"></i>
          <span slot="title">数据清洗</span>
        </el-menu-item>
        <el-menu-item index="/scimetrics/graph/index">
          <i class="el-icon-map-location"></i>
          <span slot="title">生成图表</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-main style="width:100%;height:100%;margin:0px;padding:0"><router-view /></el-main>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      activeMenu: '/scimetrics/datasource/index'
    }
  },
  mounted() {
    this.$router.push(this.activeMenu)
  },
  methods: {},
  components: {}
}
</script>

<style lang="scss" scoped></style>
