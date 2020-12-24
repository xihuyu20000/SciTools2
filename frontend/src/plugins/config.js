import Vue from 'vue'
Vue.prototype.$config = {
  title: '科研助手',
  subtitle: '做好用的科研助手',
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
    }
  }
}
