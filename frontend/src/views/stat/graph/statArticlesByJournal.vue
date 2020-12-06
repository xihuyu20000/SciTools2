<template><echarts-line :cfg="cfg"></echarts-line> </template>

<script>
import EchartsLine from '@/components/graph/EchartsLine'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/statArticlesByJournal/a1738a9d2b1511eb9066e8b1fca4ff37'
      }
    }
  },
  components: { EchartsLine }
}
</script>

<style></style>
