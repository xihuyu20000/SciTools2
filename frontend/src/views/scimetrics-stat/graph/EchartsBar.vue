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
    }
  },
  mounted() {
    this.fetch()
  }
}
</script>

<style lang="scss" scoped></style>
