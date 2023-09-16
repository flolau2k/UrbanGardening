<script setup lang="ts">
const takePhoto = (): void => {
  alert('SIKE! Not implemented yet.')
}

const startTimelapse = (): void => {
  alert('SIKE! Not implemented yet.')
}
</script>

<template>
  <div class="w-[420px] h-[230px] rounded-lg relative group">
    <div
      class="h-full w-full bg-center rounded-lg bg-cover z-0"
      style="background-image: url('../../src/assets/login-picture.png')"
    ></div>
    <div
      class="absolute inset-0 bg-black rounded-lg opacity-0 group-hover:opacity-50 transition-opacity duration-300 z-10"
    ></div>
    <div
      class="absolute inset-0 z-20 flex gap-x-5 justify-center items-center opacity-0 group-hover:opacity-100 transition-opacity duration-300"
    >
      <button class="bg-white/80 p-2 rounded-lg cursor-pointer" @click="takePhoto">
        Take Photo
      </button>
      <button class="bg-white/80 p-2 rounded-lg cursor-pointer" @click="startTimelapse">
        Timelapse
      </button>
    </div>
  </div>
</template>
