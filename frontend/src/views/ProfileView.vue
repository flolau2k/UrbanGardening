<script setup lang="ts">
import CustomButton from '../components/CustomButton.vue';
import CustomInput from '../components/CustomInput.vue';
</script>

<template>
  <div class="flex items-center justify-center h-full">
    <div class="w-1/3 h-1/3 p-4 bg-white rounded-md">
      <div class=" text-teal-500 text-2xl font-bold">Values</div>
      <div class="pt-5">
        <CustomInput name="Item 1" label="Item 1" class="pb-2" />
        <CustomInput name="Item 2" label="Item 2" class="pb-2" />
        <CustomInput name="Item 3" label="Item 3" class="pb-2" />
        <CustomButton button-name="Update" />
      </div>
    </div>
  </div>
</template>
