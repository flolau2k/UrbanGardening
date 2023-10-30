<script setup lang="ts">
import { RouterView, useRoute } from 'vue-router'
import NavBar from './components/NavBar.vue'

const route = useRoute()
</script>

<template>
  <div :class="`min-w-screen min-h-screen ${route.name != 'login' ? 'bg-colour' : 'bg-colour-login'}`">
    <NavBar v-if="route.name != 'login'" />
    <div :class="` ${route.name != 'login' ? 'pt-20 p-5' : ''} `">
      <RouterView />
    </div>
  </div>
</template>
