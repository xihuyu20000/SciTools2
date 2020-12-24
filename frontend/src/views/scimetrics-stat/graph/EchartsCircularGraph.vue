<template>
  <div>
    <el-row>
      <el-col :span="2">
        <option-title :optionData="option"></option-title>
        <option-legend :optionData="option"></option-legend>
        <option-grid :optionData="option"></option-grid>
        <option-xaxis :optionData="option"></option-xaxis>
        <option-yaxis :optionData="option"></option-yaxis>
      </el-col>
      <el-col :span="22"><chart :options="option"></chart></el-col>
      <el-col :span="0"></el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  props: ['cfg'],
  data: function() {
    return {
      myChart: '',

      option: {
        title: {
          text: 'Les Miserables',
          subtext: 'Circular layout',
          top: 'bottom',
          left: 'right'
        },
        tooltip: {},
        legend: [
          {
            data: []
          }
        ],
        animationDurationUpdate: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [
          {
            name: 'Les Miserables',
            type: 'graph',
            layout: 'circular',
            circular: {
              rotateLabel: true
            },
            data: [],
            links: [],
            categories: [],
            roam: true,
            label: {
              position: 'right',
              formatter: '{b}'
            },
            lineStyle: {
              color: 'source',
              curveness: 0.3
            }
          }
        ]
      }
    }
  },
  watch: {},
  methods: {
    async fetch() {
      const { data: data } = await this.$http.get(this.cfg.url)
      this.option = data.option
      this.$bus.$emit('refresh', this.option)
    }
  },
  mounted() {
    self.myChart = this.$echarts.init(document.getElementById('chart'), null, { renderer: 'svg' })
    this.$bus.$on('refresh', option => {
      self.myChart.setOption(option)
    })
    this.fetch()

    window.addEventListener('resize', () => {
      self.myChart.resize()
    })
  }
}
</script>

<style lang="scss" scoped></style>
