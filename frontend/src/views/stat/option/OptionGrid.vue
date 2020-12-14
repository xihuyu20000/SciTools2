<template>
  <div>
    <el-form label-width="80px" label-suffix=":">
      <el-popover placement="bottom" width="400" trigger="click">
        <el-form-item label="距上">
          <el-slider v-model.number="option.grid.top"></el-slider>
        </el-form-item>
        <el-form-item label="距右">
          <el-slider v-model.number="option.grid.right"></el-slider>
        </el-form-item>
        <el-form-item label="距下">
          <el-slider v-model.number="option.grid.bottom"></el-slider>
        </el-form-item>
        <el-form-item label="距左">
          <el-slider v-model.number="option.grid.left"></el-slider>
        </el-form-item>
        <el-form-item label="高度">
          <el-input v-model="option.grid.height"></el-input>
        </el-form-item>
        <el-form-item label="宽度">
          <el-input v-model="option.grid.width"></el-input>
        </el-form-item>
        <el-button slot="reference">网格</el-button>
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
        grid: {
          left: 10,
          top: 60,
          right: 10,
          bottom: 60,
          width: 'auto',
          height: 'auto'
        }
      }
    }
  },
  watch: {
    'option.grid.top': function() {
      this.$bus.$emit('refresh', this.option)
    },
    'option.grid.right': function() {
      this.$bus.$emit('refresh', this.option)
    },
    'option.grid.bottom': function() {
      this.$bus.$emit('refresh', this.option)
    },
    'option.grid.left': function() {
      this.$bus.$emit('refresh', this.option)
    },
    'option.grid.width': function() {
      this.$bus.$emit('refresh', this.option)
    },
    'option.grid.height': function() {
      this.$bus.$emit('refresh', this.option)
    }
  }
}
</script>

<style lang="scss" scoped></style>
