<template>
  <div id="app">
    <!--<img class="logo" src="./assets/vue.png">-->
    <!--<br>-->
    <!--<img class="logo" src="./assets/dj.png">-->
    <!--<div id="top">-->
      <!--&lt;!&ndash;<hello></hello>&ndash;&gt;-->
      <!--&lt;!&ndash;<add-class></add-class>&ndash;&gt;-->
      <!--<top-bar></top-bar>-->
    <!--</div>-->

    <top-bar></top-bar>

    <!--<year></year>-->
    <!--<year></year>-->
    <!--<year></year>-->
    <!--<year></year>-->

    <div>
      <!--<year v-for="year in years" :year="year"></year>-->
      <main></main>
    </div>
    <!--<p>-->
      <!--Welcome to your poop - Vue.js app!-->
    <!--</p>-->
  </div>
</template>

<script>
import Hello from './components/Hello'
import AddClass from './components/AddClass'
import Main from './components/Main'
import TopBar from './components/TopBar'

export default {
  components: {
    Hello,
    AddClass,
    Main,
    TopBar
  }
}
</script>

<style>

  @font-face {
    font-family: "KG Second Chances Sketch";,
    src: "./assets/KGSecondChancesSketch.ttf";
  }

html {
  height: 100%;
  background-color: #4b65af;
  font-size: 62.5%;
}

body {
  display: flex;
  /*align-items: center;*/
  /*justify-content: center;*/
  height: 100%;
  margin: 0;
}

/*p {*/
  /*padding: 0;*/
  /*margin: 0;*/
/*}*/

#app {
  /*background-color: #0b97c4;*/
  color: #FFFFFF;
  /*margin-top: -100px;*/
  width: 100%;
  height: 100%;
  margin: 0;
  font-family: "KG Second Chances Sketch", sans-serif;
  text-align: left;
}

#app a {
  color: #FFFFFF;
  text-decoration: none;
}

.logo {
  width: 100px;
  height: 100px
}

#top {
  display: flex;
  align-items: center;
  /*position: fixed;*/
  /*width: 100%;*/
}

main {
  margin-top: 10rem;
}
</style>
