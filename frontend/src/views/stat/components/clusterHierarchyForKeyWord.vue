<template><cluster-hierarchy-graph :cfg="cfg"></cluster-hierarchy-graph> </template>

<script>
import ClusterHierarchyGraph from '../graph/ClusterHierarchyGraph'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/cluster/hierarchy/keyword/' + this.$route.params.dsid
      }
    }
  },
  components: { ClusterHierarchyGraph }
}
</script>

<style></style>
