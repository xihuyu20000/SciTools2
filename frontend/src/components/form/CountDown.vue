<template>
  <div id="app">
    <h3>剩余时间：{{ `${day}天 ${hr}小时 ${min}分 ${sec}秒` }}</h3>
  </div>
</template>

<script>
export default {
  props: ['period'],
  data() {
    return { end: new Date(), day: 0, hr: 0, min: 0, sec: 0 }
  },
  mounted: function() {
    this.end = Date.parse(new Date(new Date().setMinutes(new Date().getMinutes() + this.period)))
    this.countdown()
  },
  methods: {
    countdown: function() {
      const now = Date.parse(new Date())
      const msec = this.end - now
      let day = parseInt(msec / 1000 / 60 / 60 / 24)
      let hr = parseInt((msec / 1000 / 60 / 60) % 24)
      let min = parseInt((msec / 1000 / 60) % 60)
      let sec = parseInt((msec / 1000) % 60)
      this.day = day
      this.hr = hr > 9 ? hr : '0' + hr
      this.min = min > 9 ? min : '0' + min
      this.sec = sec > 9 ? sec : '0' + sec
      const that = this
      setTimeout(function() {
        that.countdown()
      }, 1000)
    }
  }
}
</script>

<style lang="scss" scoped>
#app {
  display: inline-block;
  font-size: 20px;
  font-weight: 900;
}
</style>
