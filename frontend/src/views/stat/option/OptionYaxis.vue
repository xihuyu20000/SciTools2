<template>
  <div>
    <el-form label-width="80px" label-suffix=":">
      <el-popover placement="bottom" width="400" trigger="click">
        <el-form-item label="是否显示">
          <el-switch v-model="option.yAxis.show" active-text="显示" inactive-text="隐藏"> </el-switch>
        </el-form-item>
        <el-form-item label="纵轴名称">
          <el-input v-model="option.yAxis.name"></el-input>
        </el-form-item>
        <el-form-item label="位置">
          <el-radio-group v-model="option.yAxis.nameLocation">
            <el-radio label="start">开始</el-radio>
            <el-radio label="middle">中间</el-radio>
            <el-radio label="end">末尾</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="字体大小"></el-form-item>
        <el-slider v-model.number="option.yAxis.axisLabel.fontSize"></el-slider>
        <el-button slot="reference">纵轴</el-button>
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
        yAxis: {
          show: true,
          name: '',
          nameLocation: 'start',
          axisLabel: {}
        }
      }
    }
  },
  watch: {
    optionData: function(oldVal, newVal) {
      console.log(oldVal, newVal)
      this.option.yAxis.name = oldVal.yAxisName
    },
    'option.yAxis.show': function() {
      this.$bus.$emit('refresh', this.option)
    },
    'option.yAxis.name': function() {
      this.$bus.$emit('refresh', this.option)
    },
    'option.yAxis.nameLocation': function() {
      this.$bus.$emit('refresh', this.option)
    },
    'option.yAxis.axisLabel.fontSize': function() {
      this.$bus.$emit('refresh', this.option)
    }
  }
}
</script>

<style lang="scss" scoped></style>
