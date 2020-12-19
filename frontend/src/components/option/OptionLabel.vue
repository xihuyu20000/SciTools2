<template>
  <div>
    <el-form label-width="80px" label-suffix=":">
      <el-popover placement="bottom" width="400" trigger="click">
        <el-form-item label="是否显示">
          <el-switch v-model="option.series[0].itemStyle.normal.label.show" @change="change_series_label_show"></el-switch>
        </el-form-item>
        <el-form-item label="字体大小">
          <el-slider v-model.number="option.series[0].itemStyle.normal.label.fontSize" @change="change_series_label_fontSize"> </el-slider>
        </el-form-item>
        <el-form-item label="字体颜色">
          <el-color-picker v-model="option.series[0].itemStyle.normal.label.color" @change="change_series_label_color"></el-color-picker>
        </el-form-item>
        <el-form-item label="数据样式">
          <el-input v-model="option.tooltip.formatter"></el-input>
        </el-form-item>
        <el-button slot="reference">标签</el-button>
      </el-popover>
    </el-form>
  </div>
</template>

<script>
export default {
  props: ['option'],
  data() {
    return {}
  },
  watch: {
    // 标签
    'option.tooltip.formatter': function() {
      this.$echart.refresh(this.option)
    }
  },
  methods: {
    change_series_label_show(v) {
      this.option.series[0].itemStyle.normal.label.show = v
      this.$echart.refresh(this.option)
    },
    change_series_label_fontSize(v) {
      this.option.series[0].itemStyle.normal.label.fontSize = v
      this.$echart.refresh(this.option)
    },
    change_series_label_color(v) {
      this.option.series[0].itemStyle.normal.label.color = v
      this.$echart.refresh(this.option)
    }
  }
}
</script>

<style lang="scss" scoped></style>
