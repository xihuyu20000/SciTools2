<template><cluster-graph :cfg="cfg"></cluster-graph> </template>

<script>
import ClusterGraph from '../graph/ClusterGraph'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/cluster/spectral/keyword/' + this.$route.params.dsid
      }
    }
  },
  components: { ClusterGraph }
}
</script>

<style></style>
