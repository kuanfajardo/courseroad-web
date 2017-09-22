<template>
  <div class="year">
    <span>
      {{year}}
    </span>
    <br>
    <semester v-for="semester in sem"
              :name="semester['name']"
              :id="semester['name'].toLowerCase()"
              :hidden="semester['hidden']">

    </semester>


    <!--<semester name="Freshman Spring"></semester>-->
  </div>
</template>

<script>
  import Semester from './Semester'

  export default {
    data () {
      return {
        sem: [
          {
            name: 'Fall',
            hidden: false
          },
          {
            name: 'IAP',
            hidden: false
          },

          {
            name: 'Spring',
            hidden: false
          }
        ]
      }
    },

    components: {
      Semester
    },

    props: [
      'semesters', 'year'
    ]
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .year {
    margin-top: 3rem;
    display: flex;
    flex-wrap: wrap;
    margin-left: 3rem;
    max-width: 100%;
  }

  #fall {
    background-color: #f7e1b5;
  }

  #spring {
    background-color: #00d6b2;
  }

  #iap {
    background-color: #cee0f3;
  }

  span {
    width: 100%;
    font-size: 2.5em;
  }

</style>
