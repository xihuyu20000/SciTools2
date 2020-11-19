<template>
  <el-dialog :title="creatable ? '创建' : '修改' + globalConfig.label" :visible.sync="isShow" @close="close">
    <el-form :model="formData" ref="form1" :rules="rules">
      <el-form-item v-for="(field, index) in formConfig" :label="field.label" :label-width="field.width" :key="index" :prop="field.field">
        <form-textline :formData="formData" :field="field" />
        <form-textarea :formData="formData" :field="field" />
        <form-select-list :formData="formData" :field="field" />
        <form-select-tree :formData="formData" :field="field" />
        <form-radio :formData="formData" :field="field" />
        <form-date :formData="formData" :field="field" />
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="close">取 消</el-button>
      <el-button type="primary" @click="save">保 存</el-button>
    </div>
  </el-dialog>
</template>

<script>
export default {
  props: ['config'],
  data() {
    return {
      creatable: true,
      isShow: false,
      formData: { type: Object, required: true },
      rules: {},
      globalConfig: {},
      formConfig: []
    }
  },
  watch: {
    config: function(newVal) {
      this.globalConfig = newVal.globalConfig
      this.formConfig = newVal.formConfig
    },
    formConfig: function(newVal) {
      let _this = this
      newVal.forEach(function(field) {
        _this.rules[field.field] = field.rule
      })
    }
  },
  methods: {
    show() {
      this.isShow = true
    },
    close() {
      this.reset()
      this.isShow = false
    },
    reset() {
      this.$refs['form1'].resetFields()
    },
    async save() {
      this.$refs['form1'].validate(async valid => {
        if (!valid) return false
        let _resp = undefined
        if (this.creatable) {
          let data = await this.$http.post(this.globalConfig.url, this.formData)
          _resp = data.data
        } else {
          let data = await this.$http.put(this.globalConfig.url + '/' + this.formData.id, this.formData)
          _resp = data.data
        }
        if (_resp.status != 200) return this.$message.error(_resp.msg)
        this.$bus.$emit(this.$bus.loadData)
        this.close()
      })
    }
  },
  mounted() {
    this.$bus.$on(this.$bus.showCreateDialog, () => {
      this.isShow = true
      this.creatable = true
    })
    this.$bus.$on(this.$bus.showEditDialog, row => {
      this.isShow = true
      this.creatable = false
      this.formData = row
    })
  }
}
</script>

<style lang="scss" scoped></style>
