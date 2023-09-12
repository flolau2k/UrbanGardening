
<script setup lang="ts">
  import StatusSquare from '../components/status.vue';
  import CameraComponent from '../components/camera.vue';
  import DropDown from '../components/DropDown.vue';
  import { DropDownData } from '../../types/DropDownData';

  const mockDataDropdown: DropDownData[] = [{id: 1, itemName: "item 1"}, {id: 1, itemName: "item 2"}]
</script>

<template>
  <StatusSquare />
  <DropDown dropdownName="Button" :data="mockDataDropdown" />
  <CameraComponent/>
</template>
