<template>
  <div>
    <el-form label-width="80px" label-suffix=":">
      <el-popover placement="bottom" width="400" trigger="click">
        <el-form-item label="是否显示">
          <el-switch v-model="option.title.show" active-text="显示" inactive-text="隐藏"> </el-switch>
        </el-form-item>
        <el-form-item label="标题名称">
          <el-input v-model="option.title.text"></el-input>
        </el-form-item>
        <el-form-item label="字体大小">
          <el-slider v-model.number="option.title.textStyle.fontSize"></el-slider>
        </el-form-item>
        <el-form-item label="字体颜色">
          <el-color-picker v-model="option.title.textStyle.color"></el-color-picker>
        </el-form-item>
        <el-button slot="reference">标题</el-button>
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
        title: {
          show: true,
          text: '',
          textStyle: {
            color: '#333',
            fontSize: 18
          }
        }
      }
    }
  },
  watch: {
    optionData: function(oldVal, newVal) {
      console.log(oldVal, newVal)
      this.option.title.text = oldVal.option.title.text
    },
    // 是否显示标题组件
    'option.title.show': function() {
      this.$bus.$emit('refresh', this.option)
    },
    // 主标题文本，支持\n 换行
    'option.title.text': function() {
      this.$bus.$emit('refresh', this.option)
    },
    // 主标题文字的字体大小，默认是18
    'option.title.textStyle.fontSize': function() {
      this.$bus.$emit('refresh', this.option)
    },
    // 主标题文字的默认颜色，默认是#333
    'option.title.textStyle.color': function() {
      this.$bus.$emit('refresh', this.option)
    }
  },
  mounted() {}
}
</script>

<style lang="scss" scoped></style>
