<template><echarts-word-clound :cfg="cfg"></echarts-word-clound> </template>

<script>
import EchartsWordClound from '../graph/EchartsWordClound'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/wordclound/keyword/' + this.$route.params.dsid
      }
    }
  },
  components: { EchartsWordClound }
}
</script>

<style></style>
