<template>
  <!--<div class="cr-button">-->
  <!--</div>-->
  <button type="button" :id="buttonId">{{title}}</button>
</template>

<script>
  export default {
    name: 'round-button',

    data () {
      return {
        msg: 'msg'
      }
    },

    props: ['button-id', 'title']
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #login-button {
    background-color: #00d4b4;
    left: 57rem;
  }

  #settings-button {
    background-color: lightcoral;
    left: 52rem;
  }

  #add-button {
    background-color: #0b97c4;
    left: 46rem;
  }

  button {
    position: relative;
    color: #FFFFFF;
    font-size: 1.5rem;
    font-family: "KG Second Chances Sketch", sans-serif;
    border: none;
    border-radius: 4pt;
    padding: 1.2rem 1.5rem;
    outline: none;
  }

  button:hover {
    border-style: solid;
    border-color: white;
  }

</style>