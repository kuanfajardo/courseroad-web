<template>
  <button type="button" class=class-button :class="{ok: !hasConflict, red: hasConflict}" draggable="true"></button>
</template>

<script>
  export default {
    name: 'class-button',

    data () {
      return {
        msg: 'msg'
      }
    },

    props: ['hasConflict']
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .class-button {
    /*position: relative;*/
    color: #FFFFFF;
    font-size: 1.5rem;
    font-family: "KG Second Chances Sketch", sans-serif;
    border: none;
    border-radius: 4pt;
    padding: 1.2rem 1.5rem;
    outline: none;
    width: 11rem;
    height: 6rem;
  }

  .ok {
    background-color: #f0e9df;
  }

  .red {
    background-color: lightcoral;
  }

  button:hover {
    border-style: solid;
    border-color: white;
  }

</style>
