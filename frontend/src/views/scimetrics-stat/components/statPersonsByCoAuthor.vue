<template><echarts-stack-bar :cfg="cfg"></echarts-stack-bar> </template>

<script>
import EchartsStackBar from '../graph/EchartsStackBar'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/statPersonsByCoAuthor/' + this.$route.params.dsid
      }
    }
  },
  components: { EchartsStackBar }
}
</script>

<style></style>
