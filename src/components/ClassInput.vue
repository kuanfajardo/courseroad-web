<template>
  <input class="class-input" type="text" placeholder="Add Classes...">
</template>

<script>
  export default {
    name: 'class-input',

    data () {
      return {
        msg: 'msg'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .class-input {
    position: relative;
    background-color: #d9edf7;
    border-style: solid;
    border-radius: 3em;
    border-color: black;
    height: 1.5em;
    margin: 0;
    left: 40rem;
    padding: 0.75rem 1.5rem;
    width: 20%;
    font-size: 1.5rem;
    font-family: "KG Second Chances Sketch", sans-serif;
    outline: none;
  }
</style>
