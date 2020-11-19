<template>
  <tooltip :field="field"><el-input v-if="field.style == 'textline'" v-model="formData[field.field]" autocomplete="off" :placeholder="field.label"></el-input></tooltip>
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
