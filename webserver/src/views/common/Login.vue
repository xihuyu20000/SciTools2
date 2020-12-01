<template>
  <div class="login-container">
    <div class="login-box">
      <el-form :model="loginForm" status-icon :rules="rules" ref="loginForm" label-width="0px" class="login-form" size="large"
        ><h2 style="text-align:center">{{ this.$config.title }}</h2>
        <el-form-item prop="username">
          <el-input prefix-icon="iconfont aliuser" v-model="loginForm.username" placeholder="用户名" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input prefix-icon="iconfont alilock" type="password" v-model="loginForm.password" placeholder="密码" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item class="actions">
          <el-button type="primary" @click="submitForm('loginForm')">登录</el-button>
          <el-button @click="resetForm('loginForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loginForm: {
        username: 'root',
        password: 'admin'
      },
      rules: {
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
      }
    }
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(async valid => {
        if (!valid) return false
        const { data: resp } = await this.$http.post(this.$api.login, this.loginForm)
        if (resp.status == 400) return this.$message.error(resp.msg)
        // 写入session
        window.sessionStorage.setItem('token', resp.token)
        // 获取导航菜单
        const { data: resp1 } = await this.$http.get(this.$api.navs)
        localStorage.setItem('menuTree', JSON.stringify(resp1.data))
        // this.$store.commit("home/setMenuTree", resp1.data);
        // 动态添加路由 ，参考https://refined-x.com/2017/09/01/%E7%94%A8addRoutes%E5%AE%9E%E7%8E%B0%E5%8A%A8%E6%80%81%E8%B7%AF%E7%94%B1/
        // this.$router.addRoutes([])
        // 转向主页
        this.$router.push('/')
        this.$notify({
          title: '登录成功',
          message: '欢迎登录系统',
          position: 'bottom-right',
          type: 'success'
        })
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style lang="scss" scoped>
.image {
  height: 100vh;
}
.login-container {
  .login-box {
    height: 100vh;
    background-color: #eee;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

    .el-form {
      width: 400px;
      height: 250px;
      padding: 20px;
      background-color: bisque;
      border-radius: 10px;
      h2 {
      }
      .actions {
        display: flex;
        justify-content: space-evenly;
      }
    }
  }
}
</style>
