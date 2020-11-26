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
        <el-menu :default-active="activeTopMenu" mode="horizontal" background-color="#1890ff" text-color="#fff" active-text-color="#ffd04b" @select="headerNav">
          <el-menu-item v-for="nav in headerMenus" :index="nav.id + ''" :key="nav.id">{{ nav.label }}</el-menu-item>
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
      <el-aside :width="collapsed ? '64px' : '200px'" style="background-color: rgb(238, 241, 246)">
        <el-menu router :default-active="activeLeftActive" :unique-opened="true" :collapse="collapsed" :collapse-transition="false" size="mini">
          <el-menu-item index="/default"><i class="el-icon-s-home"></i><span v-show="!collapsed">首页</span></el-menu-item>
          <el-submenu :index="menu1.id + ''" v-for="menu1 of leftMenus" :key="menu1.id">
            <template slot="title"
              ><i :class="menu1.icon"></i><span v-show="!collapsed">{{ menu1.label }}</span></template
            >
            <el-menu-item :index="menu2.path" v-for="menu2 of menu1.children" :key="menu2.id" @click="selectLeftMenu(menu2)">{{ menu2.label }}</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <el-tabs editable v-model="activeTabName" @tab-click="selectTab" @tab-remove="removeTab">
          <el-tab-pane label="首页" name="首页" closable></el-tab-pane>
          <el-tab-pane v-for="item in tabs" :label="item.label" :name="item.name" :key="item.label"></el-tab-pane>
        </el-tabs>
        <router-view
      /></el-main>
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
      headerMenus: [],
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
    headerNav(index) {
      sessionStorage.setItem('top_menu', index)
      let m = this.menuTree.filter(item => item.id == index)
      if (m[0].children) this.leftMenus = m[0].children
      else this.leftMenus = []
    },
    chpwd() {
      this.$message.success('修改密码')
    },
    showprofile() {
      this.$message.success('显示个人用户')
    },
    logout() {
      window.sessionStorage.clear()
      this.$router.push('/login')
    },
    selectLeftMenu(menu) {
      if (!menu.path) return this.$message.error('没有配置菜单路径')
      this.activeLeftActive = menu.path
      sessionStorage.setItem('active_left_menu', this.activeLeftActive)
      // 判断是否已经打开该菜单
      let existed = this.tabs.filter(item => item.label == menu.label)
      if (existed.length == 0) {
        this.tabs.push({ label: menu.label, name: this.activeLeftActive })
      }
      this.activeTabName = this.activeLeftActive
    },
    selectTab() {
      this.$router.push(this.activeTabName)
      sessionStorage.setItem('active_left_menu', this.activeTabName)
    },
    removeTab(targetName) {
      let tabs = this.tabs
      let _activeName = this.activeTabName
      if (_activeName === targetName) {
        tabs.forEach((tab, index) => {
          if (tab.name === targetName) {
            let nextTab = tabs[index + 1] || tabs[index - 1]
            if (nextTab) {
              _activeName = nextTab.name
            }
          }
        })
      }

      this.activeName = _activeName
      this.tabs = tabs.filter(tab => tab.name !== targetName)
    }
  },
  created() {
    // 加载全部菜单
    this.menuTree = JSON.parse(localStorage.getItem('menuTree'))
    // 过滤顶级菜单
    this.headerMenus = this.menuTree.filter(item => item.pid == 0)
    // 顶级激活菜单
    this.activeTopMenu = sessionStorage.getItem('top_menu') || '1'
    // 导航左侧菜单
    this.headerNav(this.activeTopMenu)
    // 左侧激活菜单
    this.activeLeftActive = sessionStorage.getItem('active_left_menu')
    // 显示tab
    // this.selectTab()
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
