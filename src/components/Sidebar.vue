<template>
  <div class="sidebar">
    <div id="title">Requirements</div>
  </div>
</template>

<script>
  import VueSticky from 'vue-sticky'
  const v = VueSticky.default

  export default {
    data () {
      return {
        msg: 'msg'
      }
    },

    directives: {
      'sticky': v
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .sidebar {
    position: fixed;
    border-style: solid;
    border-width: 0.7em;
    /*background-color: #5e67b4;*/
    border-color: #91d2ff;
    /*background-color: #8a95ff;*/
    left: 80%;
    /*float: right;*/
    right: 2%;
    top: 15%;
    bottom: 5%;
    margin-top: 3em;
    border-radius: 2em;
    padding: 2em;
  }

  #title {
    text-align: center;
    font-size: 2em;
  }

</style>
