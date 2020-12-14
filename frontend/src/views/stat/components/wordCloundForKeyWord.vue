<template><word-clound :cfg="cfg"></word-clound> </template>

<script>
import WordClound from '../graph/WordClound'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/stat/wordclound/keyword/' + this.$route.params.dsid
      }
    }
  },
  components: { WordClound }
}
</script>

<style></style>
