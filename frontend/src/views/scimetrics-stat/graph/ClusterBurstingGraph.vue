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
// echarts中，阶梯瀑布图
<script>
export default {
  props: ['cfg'],
  data: function() {
    return {
      optionData: {},
      option: {
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
          trigger: 'axis',
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          },
          formatter: function(params) {
            var tar
            if (params[1].value !== '-') {
              tar = params[1]
            } else {
              tar = params[0]
            }
            return tar.name + '<br/>' + tar.seriesName + ' : ' + tar.value
          }
        },
        legend: {
          data: ['上升', '下降']
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        yAxis: {
          type: 'category',
          splitLine: { show: false },
          data: (function() {
            var list = ['大数据', '数字人文', '数字图书馆', '智慧图书馆', '可视化', '知识图谱', '科学计量', '阅读推广', '公共图书馆', '十四五规划', '用户服务']
            return list
          })()
        },
        xAxis: {
          type: 'value'
        },
        series: [
          {
            name: '辅助',
            type: 'bar',
            stack: '总量',
            itemStyle: {
              barBorderColor: 'rgba(0,0,0,0)',
              color: 'rgba(0,0,0,0)'
            },
            emphasis: {
              itemStyle: {
                barBorderColor: 'rgba(0,0,0,0)',
                color: 'rgba(0,0,0,0)'
              }
            },
            data: [0, 900, 1245, 1530, 1376, 1376, 1511, 1689, 1856, 1495, 1292]
          },
          {
            name: '上升',
            type: 'bar',
            stack: '总量',
            label: {
              show: true,
              position: 'top'
            },
            data: [900, 345, 393, '-', '-', 135, 178, 286, '-', '-', '-']
          },
          {
            name: '下降',
            type: 'bar',
            stack: '总量',
            label: {
              show: true,
              position: 'bottom'
            },
            data: ['-', '-', '-', 108, 154, '-', '-', '-', 119, 361, 203]
          }
        ]
      }
    }
  },
  watch: {},
  methods: {
    async fetch() {
      // const { data: res } = await this.$http.get(this.cfg.url)
      // this.forceData = res.data.value

      // 更新数据
      this.optionData = { option: this.option }
      // 更新图像
      this.$bus.$emit('refresh', this.option)
    }
  },
  mounted() {
    // 基于准备好的dom，初始化echarts实例
    let myChart = this.$echarts.init(document.getElementById('chart'), null, { renderer: 'svg' })
    myChart.showLoading()
    // 绘制图表
    myChart.setOption(this.option)

    window.addEventListener('resize', () => {
      myChart.resize()
    })
    this.$bus.$on('refresh', option => {
      myChart.setOption(option)
    })
    this.fetch()
    myChart.hideLoading()
  }
}
</script>

<style lang="scss" scoped></style>
