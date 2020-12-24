<template>
  <vxe-modal v-model="visible" :transfer="true" :fullscreen="true" width="100%" height="100%" min-width="400" min-height="320" :mask="true" :mask-closable="true" :esc-closable="true" show-zoom resize remember storage>
    <template v-slot:title>
      <span style="color: red;">图表设计引擎</span>
    </template>
    <template v-slot>
      <vxe-select v-model="selected_dimensions" :multi-char-overflow="-1" placeholder="多选可清除" multiple clearable>
        <vxe-option value="1" label="维度1"></vxe-option>
        <vxe-option value="2" label="维度2"></vxe-option>
      </vxe-select>
      <vxe-select v-model="selected_series" :multi-char-overflow="-1" placeholder="多选可清除" multiple clearable>
        <vxe-option value="1" label="序列1"></vxe-option>
        <vxe-option value="2" label="序列2"></vxe-option>
      </vxe-select>
      <vxe-select v-model="selected_graph" placeholder="请选择图形" prefix-icon="fa fa-user-o">
        <vxe-option value="line1" label="基本折线图"></vxe-option>
        <vxe-option value="line2" label="面积图"></vxe-option>
        <vxe-option value="line4" label="堆积面积图"></vxe-option>
        <vxe-option value="line6" label="面积碎片图"></vxe-option>
        <vxe-option value="bar1" label="柱状图"></vxe-option>
        <vxe-option value="pie1" label="饼图"></vxe-option>
      </vxe-select>
      <vxe-button icon="fa fa-graduation-cap my-green" @click="loadGraphOptionAndData">运行</vxe-button>
      <chart :options="option"></chart>
    </template>
  </vxe-modal>
</template>

<script>
export default {
  data() {
    return {
      visible: true,
      selected_dimensions: [],
      selected_series: [],
      selected_graph: '',
      option: {
        xAxis: {
          data: ['Q1', 'Q2', 'Q3', 'Q4']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            type: 'bar',
            data: [63, 75, 24, 92]
          }
        ]
      }
    }
  },
  methods: {
    async loadGraphOptionAndData() {
      // 加载并显示图表
      if (this.selected_graph == '') return this.$message.error('请选择图形类型')
      let _url = this.$api.advanced_graphs_load_option_data + '/' + this.selected_graph
      const { data: resp } = await this.$http.get(_url)
      if (resp.status == 400) return this.$message.error(resp.msg)
      this.option = resp.data.option
      console.log('配置信息', this.option)
    }
  },
  mounted() {
    this.$http.get('/static/graphoption.js').then(response => {
      console.log('本地json文件', response.data)
    })
    this.$bus.$on('show_graph_full_design', () => {
      this.visible = true
      // this.fetch()
    })
  }
}
</script>
<style>
.echarts {
  margin: 20px;
  background-color: #fff;
  width: 100%;
  height: 500px;
}
</style>
