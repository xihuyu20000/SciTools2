import Vue from 'vue'
// 这里的注册名，必须是小写，并且在调用的时候，也要小写

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

import CommonTable from './form/CommonTable'
import CommonTree from './form/CommonTree'
import CountDown from './form/CountDown'
import CreateForm from './form/CreateForm'
import DataTemplate1 from './form/DataTemplate1'
import DataTemplate2 from './form/DataTemplate2'

Vue.component('common-table', CommonTable)
Vue.component('common-tree', CommonTree)
Vue.component('count-down2', CountDown)
Vue.component('create-form', CreateForm)
Vue.component('dt1', DataTemplate1)
Vue.component('dt2', DataTemplate2)

import OptionLabel from './option/OptionLabel.vue'
import OptionLegend from './option/OptionLegend.vue'
import OptionTitle from './option/OptionTitle.vue'
import OptionXaxis from './option/OptionXaxis.vue'
import OptionYaxis from './option/OptionYaxis.vue'
import OptionGrid from './option/OptionGrid.vue'

Vue.component('option-label', OptionLabel)
Vue.component('option-legend', OptionLegend)
Vue.component('option-title', OptionTitle)
Vue.component('option-xaxis', OptionXaxis)
Vue.component('option-yaxis', OptionYaxis)
Vue.component('option-grid', OptionGrid)
