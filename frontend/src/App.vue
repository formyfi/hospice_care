<template>

<HomeApp />

</template>

<script>
import HomeApp from './components/HomeApp.vue'


export default {
    name: 'App',
    components: {
      HomeApp,
    }
}
</script>

<style>
@import '~vuetify/dist/vuetify.min.css';
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
