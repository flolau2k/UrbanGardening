<script setup lang="ts">
defineProps({
  buttonName: String
})
</script>

<template>
  <button
    class="border px-4 py-2 text-base w-full cursor-pointer hover:bg-green-300 hover:text-green-800 duration-300 ease-in-out rounded-md border-green-800 text-green-500"
    @click="$emit('customClick')"
  >
    {{ buttonName }}
  </button>
</template>
