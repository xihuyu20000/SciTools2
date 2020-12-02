<template><echarts-bar :cfg="cfg"></echarts-bar> </template>

<script>
import EchartsBar from '@/components/graph/EchartsBar'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/statArticlesByCountry/a1738a9d2b1511eb9066e8b1fca4ff37'
      }
    }
  },
  components: { EchartsBar }
}
</script>

<style></style>
