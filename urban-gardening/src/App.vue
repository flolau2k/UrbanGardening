<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue';
</script>

<template>
  <div class="flex w-full h-full">
    <NavBar />
    <div class="p-5 w-full h-full">
      <RouterView />
    </div>
  </div>
</template>
