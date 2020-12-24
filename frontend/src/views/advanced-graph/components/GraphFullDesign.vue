<template>
  <vxe-modal v-model="visible" :fullscreen="true" width="760" height="80%" min-width="400" min-height="320" :mask="true" :mask-closable="true" :esc-closable="true" show-zoom resize remember storage transfer>
    <template v-slot:title>
      <span style="color: red;">图表设计引擎</span>
    </template>
    <template v-slot>
      <vxe-select v-model="selected_dimensions" :multi-char-overflow="-1" placeholder="多选可清除" multiple clearable>
        <vxe-option value="1" label="选项1"></vxe-option>
        <vxe-option value="2" label="选项2"></vxe-option>
        <vxe-option value="3" label="选项3"></vxe-option>
        <vxe-option value="4" label="选项4"></vxe-option>
        <vxe-option value="5" label="选项5"></vxe-option>
      </vxe-select>
      <vxe-select v-model="selected_series" :multi-char-overflow="-1" placeholder="多选可清除" multiple clearable>
        <vxe-option value="1" label="选项1"></vxe-option>
        <vxe-option value="2" label="选项2"></vxe-option>
        <vxe-option value="3" label="选项3"></vxe-option>
        <vxe-option value="4" label="选项4"></vxe-option>
        <vxe-option value="5" label="选项5"></vxe-option>
      </vxe-select>
      <vxe-select v-model="selected_graph" placeholder="请选择" prefix-icon="fa fa-user-o">
        <vxe-option v-for="num in 3" :key="num" :value="num" :label="`选项${num}`"></vxe-option>
      </vxe-select>
    </template>
  </vxe-modal>
</template>

<script>
export default {
  props: ['cfg'],
  data: function() {
    return {
      visible: true,
      selected_dimensions: [],
      selected_series: [],
      selected_graph: '',
      myChart: '',
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
          interval: 1,
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
        dataset: { source: [] },
        series: [{ type: 'line' }]
        // series: [
        //   {
        //     name: '',
        //     data: [],
        //     type: 'line',
        //     itemStyle: { normal: { label: { show: true, fontSize: 20, color: '#333' } } }
        //   }
        // ]
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
    window.addEventListener('resize', () => {
      self.myChart.resize()
    })
    this.$bus.$on('show_graph_full_design', () => {
      this.visible = true
      // this.fetch()
    })
  }
}
</script>

<style lang="scss" scoped>
.vxe-input {
  width: 400px;
}

.chart {
  margin: 20px;
  background-color: #fff;
  width: 100%;
  height: 500px;
}
</style>
