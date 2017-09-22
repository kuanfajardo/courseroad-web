<template>
  <form>
    <input type="text" id="add-class" placeholder="Add Classes...">
  </form>

  <button type="button" id="login-button">Login</button>
  <button type="button" id="settings-button">Settings</button>
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

  #add-class {
    position: fixed;
    background-color: #d9edf7;
    border-style: solid;
    border-radius: 3em;
    border-color: black;
    height: 2em;
    right: 45rem;
    margin: 0;
    padding: 0.5rem 1.5rem;
    top: 3rem;
    width: 15%;
    font-size: 2rem;
    font-family: "KG Second Chances Sketch", sans-serif;
    outline: none;
  }

  #login-button {
    background-color: #00d4b4;
    right: 1em;
  }

  #settings-button {
    background-color: lightcoral;
    right: 7em;
  }

  #add-button {
    background-color: #0b97c4;
    right: 14.5em;
  }

button {
  position: fixed;
  color: #FFFFFF;
  font-size: 2rem;
  /*text-align: left;*/
  font-family: "KG Second Chances Sketch", sans-serif;
  border: none;
  border-radius: 4pt;
  padding: 2rem;
  outline: none;

  /*margin: 5rem;*/
  /*float: right;*/
  /*white-space: nowrap;*/
}

  button:hover {
    border-style: solid;
    border-color: white;
  }

</style>
