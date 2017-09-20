<template>
  <div class="semester">
    <p>{{name}}</p>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        name: 'Freshman Fall'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .semester {
    margin-top: 3rem;
    position: absolute;
    left: 2%;
    right: 2%;
    background-color: #f7e1b5;
    min-height: 75pt;
    height: 10rem;
    color: #000000;
    font-size: 2rem;
    border-radius: 7pt;
  }

  p {
    margin-left: 1%;
    margin-top: 1%;
  }



</style>
