import Vue from 'vue'
Vue.prototype.$config = {
  title: '科研助手',
  subtitle: '争取做最好用的科研助手',
  defaultOption: {
    tooltip: {
      //弹窗组件
      show: true
    },
    toolbox: {
      //可视化的工具箱
      show: true,
      feature: {
        dataView: {
          //数据视图
          show: true
        },
        restore: {
          //重置
          show: true
        },
        dataZoom: {
          //数据缩放视图
          show: true
        },
        saveAsImage: {
          //保存图片
          show: true
        }
      }
    },
    xAxis: {
      data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    },
    yAxis: {},
    series: [
      {
        name: '销量',
        type: 'line',
        data: [5, 20, 36, 10, 10, 20]
      }
    ]
  }
}
