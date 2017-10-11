<template>
  <div class="semester" :hidden="hidden">
    <p>{{name}}</p>
    <class-button></class-button>
  </div>
</template>

<script>
  import ClassButton from './ClassButton.vue'

  export default {
    data () {
      return {}
    },

    props: [
      'name', 'hidden'
    ],

    components: [ClassButton]
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .semester {
    margin: 0;
    /*position: absolute;*/
    /*left: 2%;*/
    /*right: 2%;*/
    background-color: #f7e1b5;
    min-height: 75pt;
    width: 96%;
    height: 10rem;
    color: #000000;
    font-size: 2rem;
    border-radius: 7pt;
    display: block;
  }

  p {
    margin-left: 1%;
    margin-top: 1%;
  }



</style>
