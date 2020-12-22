<template>
  <el-container>
    <el-header>
      <div class="left-header">
        <div class="big-title">
          <img :src="logo" class="logo" />
          <h3 v-show="!collapsed" style="margin:0px">
            {{ this.$config.title }}
          </h3>
          <span class="iconfont" @click="toggle"><template v-if="collapsed">&#xe86f;</template><template v-else>&#xe870;</template></span>
          <h5 class="subtitle">
            {{ this.$config.subtitle }}
          </h5>
        </div>
      </div>
      <div class="nav-header">
        <!-- 顶部导航 -->
        <el-menu router :default-active="activeTopMenu" mode="horizontal" background-color="#1890ff" text-color="#fff" active-text-color="#ffd04b">
          <el-menu-item v-for="nav in headerMenus" :index="nav.path + ''" :key="nav.id">{{ nav.label }}</el-menu-item>
        </el-menu>
      </div>
      <div class="right-header">
        <img :src="avatar" class="user-avatar" />
        <el-dropdown trigger="hover">
          <span class="el-dropdown-link" style="height:50px;margin:0px">
            <span class="welcome-user">欢迎您，王小虎</span>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item @click.native="chpwd">修改密码</el-dropdown-item>
            <el-dropdown-item @click.native="showprofile">个人主页</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <el-link class="logout" @click.native="logout"><span class="iconfont">&#xe7a1;</span>退出登录</el-link>
      </div>
    </el-header>
    <el-container>
      <router-view />
    </el-container>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      logo: require('@/assets/logo.jpg'),
      avatar: require('@/assets/images/avator.jpg'),
      collapsed: false,
      menuTree: [],
      headerMenus: [
        { label: '科学计量', path: '/scimetrics/scimetricsIndex' },
        { label: '高级图表', path: '/advanced/index' },
        { label: '生成报告', path: '/report/index' },
        { label: '配置参数', path: '/config/index' }
      ],
      activeTopMenu: '2',
      activeLeftActive: '',
      activeTabName: '首页',
      headerMenus1: [],
      leftMenus: [],
      tabs: []
    }
  },
  computed: {},
  watch: {},
  methods: {
    toggle() {
      this.collapsed = !this.collapsed
    },
    chpwd() {
      this.$message.success('修改密码')
    },
    showprofile() {
      this.$message.success('显示个人用户')
    },
    logout() {
      window.sessionStorage.clear()
      this.$router.push(this.$api.login)
    }
  },
  created() {
    // 顶级激活菜单
    this.activeTopMenu = sessionStorage.getItem('top_menu') || '1'
    // 左侧激活菜单
    this.activeLeftActive = sessionStorage.getItem('active_left_menu')
  }
}
</script>

<style lang="scss" scoped>
.el-container {
  height: 100vh;
}
.toggle {
  width: 150px;
}
.el-header {
  padding: 0;
  background-color: #1890ff;
  color: #333;
  line-height: 60px;
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
  .left-header {
    .big-title {
      display: flex;
      text-align: center;
      .logo {
        border-radius: 5px;
        box-shadow: 15px 0 15px -15px #000, -15px 0 15px -15px #000;
        margin: auto 20px;
        height: 55px;
        width: 55px;
      }
      .iconfont {
        cursor: pointer;
        font-size: 40px;
        margin-left: 50px;
        margin-right: 30px;
      }
      .subtitle {
        margin: 0px;
        font-size: 20px;
        font-family: cursive;
        color: #fff;
        text-align: center;
      }
    }
  }
  .right-header {
    margin: 0;
    padding: 0;
    display: flex;
    .user-avatar {
      width: 45px;
      height: 45px;
      border-radius: 25px;
      margin-top: 8px;
      margin-right: 10px;
    }
    .welcome-user {
      color: #fff;
      text-align: center;
    }
    .logout {
      margin-left: 40px;
      margin-right: 20px;
    }
  }
}

.el-aside {
  color: #333;
}

.el-main {
  padding: 10px;
}
</style>
