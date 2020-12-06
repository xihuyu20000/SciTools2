<template>
  <el-radio-group v-if="field.style == 'radio'" v-model="formData[field.field]">
    <el-radio v-for="item in field.options.values" :key="item" :label="item" :placeholder="field.label"></el-radio>
  </el-radio-group>
</template>

<script>
export default {
  props: {
    formData: { type: Object, required: true },
    field: {
      type: Object,
      required: true,
      default: function() {
        return {}
      }
    }
  },
  setup() {
    return {}
  }
}
</script>

<style lang="scss" scoped></style>
