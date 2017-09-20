<template>
  <button type="button" id="add-button">Add</button>
</template>

<script>
export default {
  data () {
    return {
      msg: 'msg'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#add-button {
  position: absolute;
  color: #FFFFFF;
  background-color: #00d4b4;
  font-size: 2rem;
  /*text-align: left;*/
  font-family: "KG Second Chances Sketch", sans-serif;
  border: none;
  border-radius: 4pt;
  padding: 2rem;
  /*margin: 5rem;*/
  /*float: right;*/
  right: 1em;
  /*white-space: nowrap;*/
}

/*button {*/
  /*white-space: nowrap;*/
/*}*/

</style>
