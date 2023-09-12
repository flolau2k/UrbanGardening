<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue';
</script>

<template>
  <div class="w-full h-screen">
    <NavBar />
    <div class="px-5 pb-5 pt-20 w-full h-full">
      <RouterView />
    </div>
  </div>
</template>
