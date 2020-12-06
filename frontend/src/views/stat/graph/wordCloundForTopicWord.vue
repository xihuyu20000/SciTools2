<template><word-clound :cfg="cfg"></word-clound> </template>

<script>
import WordClound from '@/components/graph/WordClound'
export default {
  data: function() {
    return {
      cfg: {
        url: '/api/wordclound/topicword/a1738a9d2b1511eb9066e8b1fca4ff37'
      }
    }
  },
  components: { WordClound }
}
</script>

<style></style>
