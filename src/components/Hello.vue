<template>
  <span class="hello">
    {{ msg }}
  </span>
</template>

<script>
export default {
  name: 'hello',
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
  font-size: 3rem;
  text-align: center;
  left: 5rem;
  /*padding-left: 20%;*/
  /*padding-right: 20%;*/
  /*margin-top: 0;*/
  /*background-color: #1A01CC;*/
  margin: 1rem 5rem 1rem 3rem;
  /*white-space: nowrap;*/
}


</style>
