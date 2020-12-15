<template><cluster-trend-graph :cfg="cfg"></cluster-trend-graph> </template>

<script>
import ClusterTrendGraph from '../graph/ClusterTrendGraph'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/cluster/trend/keyword/' + this.$route.params.dsid
      }
    }
  },
  components: { ClusterTrendGraph }
}
</script>

<style></style>
