<template><echarts-bar :cfg="cfg"></echarts-bar> </template>

<script>
import EchartsBar from '../graph/EchartsBar'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/statArticlesByPublication/' + this.$route.params.dsid
      }
    }
  },
  components: { EchartsBar }
}
</script>

<style></style>
