import Vue from 'vue'
import 'xe-utils'
import VXETable from 'vxe-table'
import 'vxe-table/lib/style.css'

// 创建一个空内容渲染
VXETable.renderer.add('NotData', {
  // 空内容模板
  renderEmpty() {
    return [
      <span>
        <img src="../assets/logo.jpg" />
        <p>亲，没有更多数据了！</p>
      </span>
    ]
  }
})

Vue.use(VXETable)
