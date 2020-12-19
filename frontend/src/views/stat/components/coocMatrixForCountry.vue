<template><echarts-cooc-matrix :cfg="cfg"></echarts-cooc-matrix> </template>

<script>
import EchartsCoocMatrix from '../graph/EchartsCoocMatrix'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/coocMatrix/country/' + this.$route.params.dsid
      }
    }
  },
  components: { EchartsCoocMatrix }
}
</script>

<style></style>
