<template><echarts-line :cfg="cfg"></echarts-line> </template>

<script>
import EchartsLine from '../graph/EchartsLine'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/statArticlesByJournal/' + this.$route.params.dsid
      }
    }
  },
  components: { EchartsLine }
}
</script>

<style></style>
