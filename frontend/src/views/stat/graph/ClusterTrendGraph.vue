<template>
  <div>
    <el-row>
      <el-col :span="1"><option-title :optionData="optionData"></option-title> </el-col>
      <el-col :span="22"><div id="chart" class="chart"></div></el-col>
      <el-col :span="1"></el-col>
    </el-row>
  </div>
</template>

<script>
var axisData = ['2001', '2002', '2003', '2004', '2005']
var data = [
  { value: '0', name: '数字图书馆学' },
  { value: '5', name: '数字人文' },
  { value: '12', name: '知识图谱' },
  { value: '30', name: '科学计量' },
  { value: '40', name: '智慧图书馆' }
]
console.log('数据', data)
var links = data.map(function(item, i) {
  return {
    source: i,
    target: i + 1
  }
})
links.pop()
console.log('连线', links)

export default {
  props: ['cfg'],
  data: function() {
    return {
      forceData: { nodes: [], edges: [] },
      optionData: {},
      option: {}
    }
  },
  watch: {},
  methods: {},
  mounted() {
    // 基于准备好的dom，初始化echarts实例
    let myChart = this.$echarts.init(document.getElementById('chart'), null, { renderer: 'svg' })
    myChart.showLoading()
    // 绘制图表
    myChart.setOption(this.option)

    window.addEventListener('resize', () => {
      myChart.resize()
    })
    this.option = {
      title: {
        text: '关键词聚类趋势图'
      },
      tooltip: {},
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: axisData
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          type: 'graph',
          layout: 'none',
          coordinateSystem: 'cartesian2d',
          animationDelay: function(idx) {
            return idx * 100
          },

          label: {
            normal: {
              position: 'right',
              formatter: '{b}',
              show: true,
              textStyle: {
                color: '#ff0000',
                fontSize: '12px',
                fontWeight: 'normal'
              }
            }
          },
          edgeSymbol: ['none', 'arrow'],
          edgeSymbolSize: [4, 10],
          data: data,
          links: links,
          roam: true,
          draggable: true,
          lineStyle: {
            color: '#2f4554',
            curveness: 0.5
          },
          itemStyle: {
            color: {
              type: 'radial',
              x: 0.5,
              y: 0.5,
              r: 0.5,
              colorStops: [
                {
                  offset: 0,
                  color: 'yellow' // 0% 处的颜色
                },
                {
                  offset: 1,
                  color: 'purple' // 100% 处的颜色
                }
              ],
              global: false // 缺省为 false
            }
          },
          symbolSize: function(value, params) {
            //改变节点大小
            var SizeList = [40, 50, 60, 70, 80]
            return SizeList[params.dataIndex % 5]
          }
        }
      ]
    }
    myChart.setOption(this.option)
    myChart.hideLoading()
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
