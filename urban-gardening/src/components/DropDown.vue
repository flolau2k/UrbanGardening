<script setup lang="ts">
import { ref } from 'vue';

  // defineProps({
    // data: DropDownData[]
  // })

  const isActive = ref<Boolean>(false);

  const toggleDropDown = () => {
    isActive.value = !isActive.value;
  }
</script>
<template>

<div class="z-20 relative">
  <button @click="toggleDropDown" class="text-white bg-blue-700 hover:bg-green-800 bg-green-600 focus:outline-none font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center">
    Dropdown button 
    <svg class="w-2.5 h-2.5 ml-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
    </svg>
  </button>
  
  <!-- Dropdown menu -->
  <div v-if="isActive" id="dropdown" class="text-black top-11 absolute h-40 z-10  shadow w-44">
      <div class="py-2 text-sm text-gray-700 bg-white rounded-lg">
        <div>
          <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Dashboard</a>
        </div>
      </div>
  </div>
</div>

</template>