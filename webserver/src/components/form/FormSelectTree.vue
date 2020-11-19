<template>
  <treeselect v-if="field.style == 'selecttree'" v-model="formData[field.field]" :default-expand-level="2" :options="field.options.values" :multiple="field.multiple" :placeholder="field.label" />
</template>

<script>
import Treeselect from '@riophae/vue-treeselect'
import '@riophae/vue-treeselect/dist/vue-treeselect.css'
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
  data() {
    return {}
  },
  components: { Treeselect }
}
</script>

<style lang="scss" scoped></style>
