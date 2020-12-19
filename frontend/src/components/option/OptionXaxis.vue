<template>
  <div>
    <el-form label-width="80px" label-suffix=":">
      <el-popover placement="bottom" width="400" trigger="click">
        <el-form-item label="是否显示">
          <el-switch v-model="option.xAxis.show" active-text="显示" inactive-text="隐藏"> </el-switch>
        </el-form-item>
        <el-form-item label="横轴名称">
          <el-input v-model="option.xAxis.name"></el-input>
        </el-form-item>
        <el-form-item label="位置">
          <el-radio-group v-model="option.xAxis.nameLocation">
            <el-radio label="start">开始</el-radio>
            <el-radio label="middle">中间</el-radio>
            <el-radio label="end">末尾</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="字体大小">
          <el-slider v-model.number="option.xAxis.axisLabel.fontSize"></el-slider>
        </el-form-item>
        <el-form-item label="字体倾斜">
          <el-slider v-model.number="option.xAxis.axisLabel.rotate"></el-slider>
        </el-form-item>
        <el-form-item label="间隔">
          <el-slider v-model.number="option.xAxis.axisLabel.interval"></el-slider>
        </el-form-item>
        <el-button slot="reference">横轴</el-button>
      </el-popover>
    </el-form>
  </div>
</template>

<script>
export default {
  props: ['optionData'],
  data() {
    return { option: { xAxis: { show: true, name: '', nameLocation: 'end', axisLabel: {} } } }
  },
  watch: {
    optionData: function(oldVal, newVal) {
      console.log(oldVal, newVal)
      this.option.xAxis.name = oldVal.xAxisName
    },
    'option.xAxis.show': function() {
      this.$bus.$emit('refresh', this.option)
    },
    'option.xAxis.name': function() {
      this.$bus.$emit('refresh', this.option)
    },
    'option.xAxis.nameLocation': function() {
      this.$bus.$emit('refresh', this.option)
    },
    'option.xAxis.axisLabel.fontSize': function() {
      this.$bus.$emit('refresh', this.option)
    },
    'option.xAxis.axisLabel.rotate': function() {
      this.$bus.$emit('refresh', this.option)
    },
    'option.xAxis.axisLabel.interval': function() {
      this.$bus.$emit('refresh', this.option)
    }
  }
}
</script>

<style lang="scss" scoped></style>
