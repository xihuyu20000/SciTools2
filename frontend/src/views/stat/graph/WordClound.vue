<!-- 参考 https://blog.csdn.net/qq_29132907/article/details/96482497 -->
<template>
  <div>
    <el-row>
      <el-col :span="1"
        ><option-title :optionData="optionData"></option-title>
        <option-grid :optionData="optionData"></option-grid>
        <option-legend :optionData="optionData"></option-legend>
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
          height: '50%',
          top: '10%',
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
          type: 'category',
          splitArea: {
            show: true
          }
        },
        yAxis: {
          type: 'category',
          splitArea: {
            show: true
          }
        },
        series: [
          {
            name: 'Punch Card',
            type: 'heatmap',

            label: {
              show: true
            },
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            },
            rotationRange: [-50, 50],
            textStyle: {
              normal: {
                color: function() {
                  return 'rgb(' + [Math.round(Math.random() * 160), Math.round(Math.random() * 160), Math.round(Math.random() * 160)].join(',') + ')'
                }
              },
              emphasis: {
                shadowBlur: 10,
                shadowColor: '#333'
              }
            },
            data: [
              {
                name: 'Authentication',
                value: 10000,
                textStyle: {
                  normal: {
                    color: 'black'
                  },
                  emphasis: {
                    color: 'red'
                  }
                }
              },
              {
                name: 'Streaming of segmented content',
                value: 6181
              },
              {
                name: 'Amy Schumer',
                value: 4386
              },
              {
                name: 'Jurassic World',
                value: 4055
              },
              {
                name: 'Charter Communications',
                value: 2467
              },
              {
                name: 'Chick Fil A',
                value: 2244
              },
              {
                name: 'Planet Fitness',
                value: 1898
              },
              {
                name: 'Pitch Perfect',
                value: 1484
              },
              {
                name: 'Express',
                value: 1112
              },
              {
                name: 'Home',
                value: 965
              },
              {
                name: 'Johnny Depp',
                value: 847
              },
              {
                name: 'Lena Dunham',
                value: 582
              },
              {
                name: 'Lewis Hamilton',
                value: 555
              },
              {
                name: 'KXAN',
                value: 550
              },
              {
                name: 'Mary Ellen Mark',
                value: 462
              },
              {
                name: 'Farrah Abraham',
                value: 366
              },
              {
                name: 'Rita Ora',
                value: 360
              },
              {
                name: 'Serena Williams',
                value: 282
              },
              {
                name: 'NCAA baseball tournament',
                value: 273
              },
              {
                name: 'Point Break',
                value: 265
              }
            ]
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
      this.option.yAxis.data = res.data.yData
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
