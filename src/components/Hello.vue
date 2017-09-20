<template>
  <span class="hello">
    {{ msg }}
  </span>
</template>

<script>
export default {
  data () {
    return {
      // note: changing this line won't causes changes
      // with hot-reload because the reloaded component
      // preserves its current state and we are modifying
      // its initial state.
      msg: 'courseroad'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello {
  color: #FFFFFF;
  font-size: 7rem;
  text-align: center;
  /*padding-left: 20%;*/
  /*padding-right: 20%;*/
  /*margin-top: 0;*/
  /*background-color: #1A01CC;*/
  margin: 1rem 5rem 0 1rem;
  /*white-space: nowrap;*/
}
</style>
