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
      forceData: { nodes: [], edges: [] },
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
      this.forceData = res.data.value

      this.option.series = [
        {
          type: 'graph',
          layout: 'force',
          draggable: true, // 节点可拖拽
          focusNodeAdjacency: true, // 鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点
          hoverAnimation: true, // 鼠标 hover 节点的提示动画效果
          label: { show: false },
          lineStyle: {
            width: 0.5,
            curveness: 0.3,
            opacity: 0.7
          },
          roam: 'move', //开启鼠标缩放和平移漫游
          force: {
            layoutAnimation: true, // 是否显示布局动画
            edgeLength: 5, // 节点之间的距离
            repulsion: 50, // 节点之间的斥力因子
            gravity: 0.5 // 向心节点的引力因子
          },
          emphasis: {
            label: {
              position: 'right',
              show: true
            }
          },
          // progressiveThreshold: 700,
          data: this.forceData.nodes.map(function(node) {
            return {
              id: node.id,
              name: node.label,
              symbol: 'circle', // 节点类型： 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
              symbolSize: node.size, // 节点标记的大小
              itemStyle: {
                color: node.color, // 颜色可以线性渐变和径向渐变，需要看api
                shadowColor: 'rgba(0, 0, 0, 0.5)', // 阴影颜色
                shadowBlur: 20 // 图形阴影的模糊大小
              }
            }
          }),
          edges: this.forceData.edges.map(function(edge) {
            return {
              source: edge.sourceID,
              target: edge.targetID
            }
          })
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
