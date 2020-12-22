<template><cluster-bursting-graph :cfg="cfg"></cluster-bursting-graph> </template>

<script>
import ClusterBurstingGraph from '../graph/ClusterBurstingGraph'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/cluster/bursting/keyword/' + this.$route.params.dsid
      }
    }
  },
  components: { ClusterBurstingGraph }
}
</script>

<style></style>
