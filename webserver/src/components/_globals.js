import Vue from 'vue'
// 这里的注册名，必须是小写，并且在调用的时候，也要小写

import OptionLabel from './echarts/options/OptionLabel.vue'
import OptionLegend from './echarts/options/OptionLegend.vue'
import OptionTitle from './echarts/options/OptionTitle.vue'
import OptionXaxis from './echarts/options/OptionXaxis.vue'
import OptionYaxis from './echarts/options/OptionYaxis.vue'
import OptionGrid from './echarts/options/OptionGrid.vue'

Vue.component('option-label', OptionLabel)
Vue.component('option-legend', OptionLegend)
Vue.component('option-title', OptionTitle)
Vue.component('option-xaxis', OptionXaxis)
Vue.component('option-yaxis', OptionYaxis)
Vue.component('option-grid', OptionGrid)

import FormDate from './form/FormDate.vue'
import FormRadio from './form/FormRadio.vue'
import FormSelectList from './form/FormSelectList.vue'
import FormSelectTree from './form/FormSelectTree.vue'
import FormTextarea from './form/FormTextarea.vue'
import FormTextline from './form/FormTextline.vue'
import Tooltip from './form/Tooltip.vue'
Vue.component('form-date', FormDate)
Vue.component('form-radio', FormRadio)
Vue.component('form-select-list', FormSelectList)
Vue.component('form-select-tree', FormSelectTree)
Vue.component('form-textarea', FormTextarea)
Vue.component('form-textline', FormTextline)
Vue.component('tooltip', Tooltip)

import CommonTable from './CommonTable'
import CommonTree from './CommonTree'
import CountDown from './CountDown'
import CreateForm from './CreateForm'
import DataTemplate1 from './DataTemplate1'
import DataTemplate2 from './DataTemplate2'

Vue.component('common-table', CommonTable)
Vue.component('common-tree', CommonTree)
Vue.component('count-down2', CountDown)
Vue.component('create-form', CreateForm)
Vue.component('dt1', DataTemplate1)
Vue.component('dt2', DataTemplate2)
