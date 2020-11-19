<template>
  <tooltip :field="field">
    <el-date-picker v-if="field.style == 'date'" v-model="formData[field.field]" type="date" :placeholder="field.label"> </el-date-picker>
  </tooltip>
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
