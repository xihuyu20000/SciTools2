<template>
  <div>
    <el-form label-width="80px" label-suffix=":">
      <el-popover placement="bottom" width="400" trigger="click">
        <el-form-item label="是否显示">
          <el-switch v-model="option.legend.show" active-text="显示" inactive-text="隐藏"> </el-switch>
        </el-form-item>
        <el-button slot="reference">图例</el-button>
      </el-popover>
    </el-form>
  </div>
</template>

<script>
export default {
  props: ['optionData'],
  data() {
    return {
      option: {
        legend: {
          show: true
        }
      }
    }
  },
  watch: {
    'option.legend.show': function() {
      this.$bus.$emit('refresh', this.option)
    }
  }
}
</script>

<style lang="scss" scoped></style>
