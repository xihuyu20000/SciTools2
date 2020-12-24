<template>
  <div id="app" style="min-width:1200">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'app',
  methods: {
    fetch() {
      setInterval(async () => {
        const { data: resp } = await this.$http.post(this.$api.token)
        if (resp.status != 200) {
          this.$router.push('/login')
          return this.$message.error('token过期，请重新登录')
        }
        if (resp.status == 200) {
          sessionStorage.setItem('token', resp.token)
        }
      }, 5000 * 12 * 60)
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
