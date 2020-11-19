<template>
  <dt1 :data="data"></dt1>
</template>

<script>
export default {
  data() {
    return {
      data: {}
    }
  },
  methods: {
    async fetch() {
      const { data: resp } = await this.$http.get('/user/meta')
      if (resp.status != 200)
        return this.$notify.error({
          title: '严重错误',
          message: '没有获取到配置信息'
        })
      this.data = resp
    }
  },
  created() {
    this.fetch()
  }
}
</script>

<style lang="scss" scoped></style>
