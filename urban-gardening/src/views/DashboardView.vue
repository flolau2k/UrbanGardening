
<script setup lang="ts">
  import StatusSquare from '../components/status.vue';
  import CameraComponent from '../components/camera.vue';
  import DropDown from '../components/DropDown.vue';
  import { DropDownData } from '../../types/DropDownData';

  const mockDataDropdown: DropDownData[] = [{id: 1, itemName: "Peppers"}, {id: 2, itemName: "Garlic"}]
</script>

<template>
  <div class="w-full">
    <DropDown dropdownName="Plant" :data="mockDataDropdown" />
    <div class="flex w-full p-10">
      <div class="flex-grow">
        <StatusSquare />
      </div>
      <div>
        <CameraComponent/>
      </div>
    </div>
  </div>
</template>
