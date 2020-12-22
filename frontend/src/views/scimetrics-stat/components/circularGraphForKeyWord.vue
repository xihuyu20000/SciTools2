<template><echarts-circular-graph :cfg="cfg"></echarts-circular-graph> </template>

<script>
import EchartsCircularGraph from '../graph/EchartsCircularGraph'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/circularGraph/keyword/' + this.$route.params.dsid
      }
    }
  },
  components: { EchartsCircularGraph }
}
</script>

<style></style>
