<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue';
</script>

<template>
  <div class="flex">
    <NavBar />
    <div class="p-5">
      <RouterView />
    </div>
  </div>
</template>
