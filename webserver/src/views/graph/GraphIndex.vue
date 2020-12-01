<template>
  <el-container>
    <el-aside width="300px">
      <div>
        <el-menu :router="true" default-active="2" class="el-menu-vertical-demo">
          <el-submenu :index="item" v-for="item in 50" :key="item">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>导航{{ item }}</span>
            </template>
            <el-menu-item :key="0" index="/graph/line/echartsLine">线性导航</el-menu-item>
            <el-menu-item :index="item - sub" v-for="sub in 10" :key="sub">选项{{ sub }}</el-menu-item>
          </el-submenu>
        </el-menu>
      </div>
    </el-aside>
    <el-main><router-view /></el-main>
  </el-container>
</template>

<script>
export default {
  components: {}
}
</script>

<style lang="scss" scoped>
.main {
  width: 100%;
}
</style>
