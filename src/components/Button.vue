<template>
    <button type="button" :class="{ ok: isOK, red: hasConflict"></button>
</template>


<style>
  button {
    position: relative;
    color: #FFFFFF;
    font-size: 1.5rem;
    font-family: "KG Second Chances Sketch", sans-serif;
    border: none;
    border-radius: 4pt;
    padding: 1.2rem 1.5rem;
    outline: none;
  }

  button:hover {
    border-style: solid;
    border-color: white;
  }
</style>