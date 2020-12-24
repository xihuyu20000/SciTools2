import Vue from 'vue'
import Echarts from 'vue-echarts'

import 'echarts/lib/component/axis'
import 'echarts/lib/component/brush'
import 'echarts/lib/component/legend'
import 'echarts/lib/component/title'
import 'echarts/lib/component/toolbox'
import 'echarts/lib/component/tooltip'
import 'echarts/lib/component/visualMap'

import 'echarts/lib/chart/bar'
import 'echarts/lib/chart/line'
import 'echarts/lib/chart/lines'
import 'echarts/lib/chart/pie'

Vue.component('chart', Echarts)
