<template>
  <tooltip :field="field"> <el-input v-if="field.style == 'textarea'" type="textarea" v-model="formData[field.field]" :placeholder="field.label"></el-input></tooltip>
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
