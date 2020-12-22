<template>
  <div>
    首页
    <table>
      <tr v-for="(v, i) in dataArr" :key="i">
        <td>{{ v.label }}</td>
      </tr>
    </table>

    <el-button @click="btn1">点击</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dataArr: [{ label: 'aaa' }, { label: 'bbb' }, { label: 'ccc' }]
    }
  },
  methods: {
    btn1() {
      let tmp = this.dataArr[1]
      this.dataArr[1] = this.dataArr[0]
      this.dataArr[0] = tmp
    }
  },
  mounted: function() {}
}
</script>

<style lang="scss" scoped></style>
