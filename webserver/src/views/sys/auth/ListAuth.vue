<template>
  <dt2 :treedata="treedata" :data="data"></dt2>
</template>

<script>
export default {
  data() {
    return {
      treedata: [],
      data: {}
    }
  },
  methods: {
    async fetch() {
      const { data: resp } = await this.$http.get('/meta/table/600')
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
