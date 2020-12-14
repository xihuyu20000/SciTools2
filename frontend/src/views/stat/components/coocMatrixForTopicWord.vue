<template><cooc-matrix :cfg="cfg"></cooc-matrix> </template>

<script>
import CoocMatrix from '../graph/CoocMatrix'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/coocMatrix/topicword/' + this.$route.params.dsid
      }
    }
  },
  components: { CoocMatrix }
}
</script>

<style></style>
