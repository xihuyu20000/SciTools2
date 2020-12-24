<template>
  <div>
    <el-button @click="openFullDesign">设计</el-button>
    <el-row>
      <el-col :span="1">
        <option-title :optionData="option"></option-title>
        <option-legend :optionData="option"></option-legend>
        <option-grid :optionData="option"></option-grid>
        <option-xaxis :optionData="option"></option-xaxis>
        <option-yaxis :optionData="option"></option-yaxis>
      </el-col>
      <!-- <el-col :span="22"><div id="chart" class="chart"></div></el-col> -->
      <el-col :span="1"></el-col>
    </el-row>
    <graph-full-design></graph-full-design>
  </div>
</template>

<script>
// import graphoption from '@/../public/static/graphoption.js'
import GraphFullDesign from './GraphFullDesign.vue'
export default {
  props: ['cfg'],
  data: function() {
    return { option: {} }
  },
  components: { GraphFullDesign },
  watch: {},
  methods: {
    openFullDesign() {
      this.$bus.$emit('show_graph_full_design')
    }
  },
  mounted() {
    // console.log('加载图表数据', graphoption)
  }
}
</script>

<style lang="scss" scoped>
.chart {
  margin: 20px;
  background-color: #fff;
  width: 100%;
  height: 500px;
}
</style>
