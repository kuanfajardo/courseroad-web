<template>
  <div class="top-bar">
    <hello></hello>
    <class-input></class-input>
    <round-button v-for="button in buttons" :title="button" :button-id="button.toLowerCase() + '-button'"></round-button>
  </div>
</template>

<script>
  import RoundButton from './RoundButton.vue'
  import ClassInput from './ClassInput.vue'
  import Hello from './Hello.vue'

  export default {
    data () {
      return {
        buttons: ['Add', 'Settings', 'Login']
      }
    },

    components: [RoundButton, ClassInput, Hello]
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .top-bar {
    position: fixed;
    padding-top: 1.3rem;
    align-content: center;
    display: flex;
    align-items: center;
    background-color: #5e67b4;
    border-style: none;

    border-bottom: solid;
    border-bottom-color: #91d2ff;
    width: 100%;
    padding-bottom: 1.5rem;
  }


</style>
