<!-- 参考 https://blog.csdn.net/qq_29132907/article/details/96482497 -->
<template>
  <div>
    <el-row>
      <el-col :span="1">
        <!-- <option-title :optionData="optionData"></option-title>
        <option-grid :optionData="optionData"></option-grid>
        <option-legend :optionData="optionData"></option-legend>
        <option-xaxis :optionData="optionData"></option-xaxis>
        <option-yaxis :optionData="optionData"></option-yaxis> -->
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
        series: [
          {
            type: 'wordCloud',

            // The shape of the "cloud" to draw. Can be any polar equation represented as a
            // callback function, or a keyword present. Available presents are circle (default),
            // cardioid (apple or heart shape curve, the most known polar equation), diamond (
            // alias of square), triangle-forward, triangle, (alias of triangle-upright, pentagon, and star.

            shape: 'circle',

            // A silhouette image which the white area will be excluded from drawing texts.
            // The shape option will continue to apply as the shape of the cloud to grow.

            // maskImage: maskImage,

            // Folllowing left/top/width/height/right/bottom are used for positioning the word cloud
            // Default to be put in the center and has 75% x 80% size.

            left: 'center',
            top: 'center',
            width: '70%',
            height: '80%',
            right: null,
            bottom: null,

            // Text size range which the value in data will be mapped to.
            // Default to have minimum 12px and maximum 60px size.

            sizeRange: [12, 60],

            // Text rotation range and step in degree. Text will be rotated randomly in range [-90, 90] by rotationStep 45

            rotationRange: [-90, 90],
            rotationStep: 45,

            // size of the grid in pixels for marking the availability of the canvas
            // the larger the grid size, the bigger the gap between words.

            gridSize: 8,

            // set to true to allow word being draw partly outside of the canvas.
            // Allow word bigger than the size of the canvas to be drawn
            drawOutOfBound: false,

            // Global text style
            textStyle: {
              normal: {
                fontFamily: 'sans-serif',
                fontWeight: 'bold',
                // Color can be a callback function or a color string
                color: function() {
                  // Random color
                  return 'rgb(' + [Math.round(Math.random() * 160), Math.round(Math.random() * 160), Math.round(Math.random() * 160)].join(',') + ')'
                }
              },
              emphasis: {
                shadowBlur: 10,
                shadowColor: '#333'
              }
            },

            // Data is an array. Each array item must have name and value property.
            data: [
              {
                name: 'Farrah Abraham',
                value: 366,
                // Style of single text
                textStyle: {
                  normal: {},
                  emphasis: {}
                }
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
    //myChart.setOption(this.option)

    window.addEventListener('resize', () => {
      myChart.resize()
    })
    this.$bus.$on('refresh', option => {
      myChart.setOption(option)
    })
    //this.fetch()
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
