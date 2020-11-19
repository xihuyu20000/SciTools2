<template>
  <div id="editor-main">
    <le-editor v-model="material.content" :hljs-css="hljsCss" :image-uploader="imageUploader" @save="saveMD"></le-editor>
  </div>
</template>

<script>
export default {
  data() {
    return {
      material: '',
      hljsCss: 'agate',
      imageUploader: {
        custom: false,
        fileType: 'file',
        fileNameType: '',
        imagePrefix: 'http://47.100.125.98', // 图片上传成功后，预览地址前缀
        type: 'server',
        url: 'http://47.100.125.98:82/upload' // 上传接口地址
      }
    }
  },
  computed: {
    material1: function() {
      return this.$store.state.material.material
    }
  },
  watch: {
    material1: function() {
      this.material = this.$store.state.material.material
    }
  },

  methods: {
    saveMD: async function(val) {
      console.log(this.material.content) // 这里是原markdown文本
      console.log(val) // 这个是解析出的html
      const { data: resp } = await this.$http.post('/material', { category_id: this.$store.state.material.leafNode.data.id, content: this.material.content, content_html: val })
      if (resp.status != 200) return this.$message.error('保存失败')
      this.$message.success('保存成功')
    }
  }
}
</script>

<style lang="scss" scoped>
#editor-main {
  color: #2c3e50;
  width: 100%;
  height: 90%;
}
</style>
