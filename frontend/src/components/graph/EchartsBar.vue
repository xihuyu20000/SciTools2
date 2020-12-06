<template>
  <div>
    <el-row>
      <el-col :span="1"
        ><option-title :optionData="optionData"></option-title>
        <option-grid :optionData="optionData"></option-grid>
        <option-xaxis :optionData="optionData"></option-xaxis>
        <option-yaxis :optionData="optionData"></option-yaxis>
      </el-col>
      <el-col :span="22"><div id="chart" class="chart"></div></el-col>
      <el-col :span="1"></el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  props: ['cfg'],
  data: function() {
    return {
      optionData: {},
      option: {
        grid: {
          show: true,
          height: 'auto',
          width: 'auto',
          top: 60,
          right: 50,
          bottom: 50,
          left: 80
        },
        title: {
          show: true,
          text: '',
          textStyle: {
            fontSize: 20,
            color: 'black'
          }
        },
        toolbox: {
          // 可视化的工具箱
          show: true,
          feature: {
            dataView: {
              // 数据视图
              show: true
            },
            restore: {
              // 重置
              show: true
            },
            dataZoom: {
              // 数据缩放视图
              show: true
            },
            saveAsImage: {
              // 保存图片
              show: true
            },
            magicType: {
              // 动态类型切换
              type: ['bar', 'line']
            }
          }
        },
        tooltip: {
          // 弹窗组件
          show: true,
          trigger: 'item',
          formatter: '{b}: {c}'
        },
        legend: {
          show: true
        },
        xAxis: {
          show: true,
          type: 'category',
          name: '',
          nameLocation: 'end',
          axisLabel: {
            rotate: 35,
            fontSize: 20,
            fontFamily: '微软雅黑',
            marginTop: '35px',
            show: true,
            interval: 0
          },
          data: []
        },
        yAxis: {
          show: true,
          name: '',
          nameLocation: 'end',
          type: 'value',
          axisLabel: {
            fontSize: 20,
            fontFamily: '微软雅黑',
            marginTop: '35px',
            show: true
          }
        },
        series: [
          {
            name: '',
            data: [],
            type: 'bar',
            showBackground: true,
            backgroundStyle: { color: 'rgba(220, 220, 220, 0.8)' }
          }
        ]
      }
    }
  },
  watch: {},
  methods: {
    async fetch() {
      const { data: res } = await this.$http.get(this.cfg.url)
      // 标题名称
      this.option.title.text = res.config.titleText
      // 横轴名称
      this.option.xAxis.name = res.config.xAxisName
      // 纵轴名称
      this.option.yAxis.name = res.config.yAxisName
      // 横轴数据
      this.option.xAxis.data = res.data.xData
      // 纵轴数据
      this.option.series = res.data.series
      // 更新数据
      this.optionData = { option: this.option }
      // 更新图像
      this.$bus.$emit('refresh', this.option)
    }
  },
  mounted() {
    // 基于准备好的dom，初始化echarts实例
    let myChart = this.$echarts.init(document.getElementById('chart'), null, { renderer: 'svg' })

    // 绘制图表
    myChart.setOption(this.option)

    window.addEventListener('resize', () => {
      myChart.resize()
    })
    this.$bus.$on('refresh', option => {
      myChart.setOption(option)
    })
    this.fetch()
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
