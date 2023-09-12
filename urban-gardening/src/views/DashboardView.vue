
<script setup lang="ts">
  import StatusComponent from '../components/StatusComponent.vue';
  import CameraComponent from '../components/CameraComponent.vue';
  import DropDown from '../components/DropDown.vue';
  import { DropDownData } from '../../types/DropDownData';
  import { StatusData } from '../../types/Status';

  const selectedPlant = (plant: DropDownData): void => {
    alert(`You selected ${plant.itemName}`);
  }
  const mockDataDropdown: DropDownData[] = [{id: 1, itemName: "Broccoli"}, {id: 2, itemName: "Garlic"}]
  const mockDataPlantStatus: StatusData = {kindOfPlants: 1, lastUpdated: new Date(), ph: 3, temperature: 36, waterConductivity: 2, waterLevel: 5}
</script>

<template>
  <div class="w-full">
    <DropDown dropdownName="Plant" :data="mockDataDropdown" @customClick="selectedPlant" />
    <div class="flex w-full p-10">
      <div class="flex-grow">
        <StatusComponent :data="mockDataPlantStatus" />
      </div>
      <div>
        <CameraComponent/>
      </div>
    </div>
  </div>
</template>
