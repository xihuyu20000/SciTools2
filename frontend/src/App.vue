<template>
  <div id="app" style="min-width:1024">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'app',
  methods: {
    fetch() {
      setInterval(async () => {
        const { data: resp } = await this.$http.get('/token')
        if (resp.status != 200) {
          this.$router.push('/login')
          return this.$message.error('token过期，请重新登录')
        }
        if (resp.status == 200) {
          sessionStorage.setItem('token', resp.token)
        }
        console.log('定时', resp)
      }, 5000 * 20 * 30)
    }
  },
  created() {
    this.fetch()
  }
}
</script>

<style>
#app {
}
</style>
