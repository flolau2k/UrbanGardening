<script setup lang="ts">
import { RouterView, useRoute } from 'vue-router'
import NavBar from './components/NavBar.vue'

const route = useRoute()
</script>

<template>
  <div :class="`w-full min-h-screen ${route.name != 'login' ? 'bg-colour' : 'bg-colour-login'}`">
    <NavBar v-if="route.name != 'login'" />
    <div :class="`px-5 pb-5 ${route.name != 'login' ? 'pt-20' : ''}  w-full h-full`">
      <RouterView />
    </div>
  </div>
</template>
