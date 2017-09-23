<template>
  <div class="main">
    <div class="years">
      <year v-for="year in years" :year="year"></year>
    </div>
    <sidebar></sidebar>
  </div>
</template>

<script>
  import Year from './Year'
  import Sidebar from './Sidebar'

  export default {
    data () {
      return {
        msg: 'msg',
        years: ['Freshman', 'Sophomore', 'Junior', 'Senior']
      }
    },

    components: {
      Year,
      Sidebar
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .main {
    width: 100%;
    display: block;
    /*margin-bottom: 5em;*/
    margin-top: 9rem;
    padding-bottom: 5em;

  }


  .years {
    width: 70%;
    float: left;
  }
</style>
