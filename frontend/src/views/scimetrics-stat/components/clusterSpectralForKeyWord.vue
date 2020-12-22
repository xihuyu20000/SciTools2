<template><cluster-spectral-graph :cfg="cfg"></cluster-spectral-graph> </template>

<script>
import ClusterSpectralGraph from '../graph/ClusterSpectralGraph'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/cluster/spectral/keyword/' + this.$route.params.dsid
      }
    }
  },
  components: { ClusterSpectralGraph }
}
</script>

<style></style>
