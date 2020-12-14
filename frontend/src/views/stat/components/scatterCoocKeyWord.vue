<template><scatter :cfg="cfg"></scatter> </template>

<script>
import Scatter from '../graph/Scatter'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/scatter/coockeyword/' + this.$route.params.dsid
      }
    }
  },
  components: { Scatter }
}
</script>

<style></style>
