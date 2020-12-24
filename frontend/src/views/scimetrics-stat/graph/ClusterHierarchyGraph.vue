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
      treeData: {},
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
          // 弹窗组件
          show: true,
          trigger: 'item',
          formatter: '{b}: {c}'
        },
        legend: {
          show: true
        },
        series: []
      }
    }
  },
  watch: {},
  methods: {
    async fetch() {
      const { data: res } = await this.$http.get(this.cfg.url)
      this.treeData = res.data.value

      this.option.series = [
        {
          type: 'tree',
          layout: 'orthogonal',
          data: [this.treeData],

          top: '1%',
          left: '7%',
          bottom: '1%',
          right: '20%',
          symbol: 'pin',
          symbolSize: 10,
          edgeShape: 'polyline',
          orient: 'RL',
          label: {
            position: 'left',
            verticalAlign: 'middle',
            align: 'right',
            fontSize: 9
          },

          leaves: {
            label: {
              position: 'right',
              verticalAlign: 'middle',
              align: 'left'
            }
          },

          expandAndCollapse: true,
          animationDuration: 550,
          animationDurationUpdate: 750
        }
      ]

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
