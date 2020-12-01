<template>
  <div style="width:100%;margin-top:10px">
    <el-row :gutter="20">
      <el-col :span="12" :offset="6">
        <el-collapse accordion>
          <el-collapse-item name="1">
            <template slot="title"><i class="header-icon el-icon-info"></i> <span class="title">停用词词典</span> </template>
            <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="stopwordsDict"> </el-input>
          </el-collapse-item>
          <el-collapse-item name="2">
            <template slot="title"><span class="title">分词词典</span> </template>
            <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="stopwordsDict"> </el-input>
          </el-collapse-item>
          <el-collapse-item name="3">
            <template slot="title"><span class="title">同义词词典</span> </template>
            <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="stopwordsDict"> </el-input>
          </el-collapse-item>
          <el-collapse-item name="4">
            <template slot="title"><span class="title">国家和地区词典</span> </template>
            <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="stopwordsDict"> </el-input>
          </el-collapse-item>
        </el-collapse> </el-col
    ></el-row>
    <el-row :gutter="20" style="margin-top:10px">
      <el-col :span="2" :offset="11">
        <el-button type="primary" size>保存</el-button>
      </el-col></el-row
    >
  </div>
</template>

<script>
export default {
  data() {
    return {
      stopwordsDict: ''
    }
  },
  methods: {}
}
</script>

<style lang="scss" scoped>
.title {
  font-size: 1.25em;
}
</style>
