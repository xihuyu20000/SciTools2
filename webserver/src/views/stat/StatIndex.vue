<template>
  <el-container>
    <el-aside width="300px">
      <div>
        <el-menu :router="true" default-active="2" class="el-menu-vertical-demo">
          <el-submenu :index="index + ''" v-for="(item, index) in menu" :key="index">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>{{ item.title }}</span>
            </template>
            <el-menu-item :index="sub.path" v-for="(sub, index) in item.children" :key="index">{{ sub.title }}</el-menu-item>
          </el-submenu>
        </el-menu>
      </div>
    </el-aside>
    <el-main><router-view /></el-main>
  </el-container>
</template>

<script>
export default {
  data: function() {
    return {
      menu: [
        {
          title: '基础指标',
          children: [
            { title: '历年发文量', path: '/stat/statArticlesByYear' },
            { title: '国家发文量', path: '/stat/statArticlesByCountry' }
          ]
        }
      ]
    }
  },
  components: {}
}
</script>

<style lang="scss" scoped>
.main {
  width: 100%;
}
</style>
