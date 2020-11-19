<template>
  <el-tooltip class="item" effect="dark" :disabled="disabled" :content="field.tip" placement="bottom">
    <slot></slot>
  </el-tooltip>
</template>

<script>
export default {
  props: {
    field: {
      style: Object,
      required: true
    }
  },
  computed: {
    disabled: function() {
      return (
        // eslint-disable-next-line no-prototype-builtins
        !this.field.hasOwnProperty('tip') || this.field.tip == undefined || this.field.tip == null
      )
    }
  },
  data: function() {
    return {}
  }
}
</script>

<style lang="scss" scoped></style>
