<script setup lang="ts">
import type { StatusData } from '../../types/Status'
import StatusIcon from '../components/icons/StatusIcon.vue'
import PlantStatusItem from './PlantStatusItem.vue'
import WaterIcon from './icons/WaterIcon.vue'
import ChemicalIcon from './icons/ChemicalIcon.vue'
import ElectricityIcon from './icons/ElectricityIcon.vue'
import TemperatureIcon from './icons/TemperatureIcon.vue'
import DownloadIcon from './icons/DownloadIcon.vue'

const props = defineProps<{
  data: StatusData
}>()
</script>

<template>
  <div class="bg-white w-[420px] h-[230px] p-4 rounded-lg">
    <div class="flex text-teal-500 flex-grow items-center gap-x-3">
      <div>
        <StatusIcon class="w-10 h-10" />
      </div>
      <div class="text-2xl font-bold">Plant Status</div>
    </div>
    <div class="pt-3 text-sm">
      <PlantStatusItem itemName="Water Level" :itemValue="props.data.waterLevel.toString()">
        <WaterIcon class="w-4 h-4" />
      </PlantStatusItem>
      <PlantStatusItem itemName="PH Level" :itemValue="props.data.ph.toString()">
        <ChemicalIcon class="w-4 h-4" />
      </PlantStatusItem>
      <PlantStatusItem
        itemName="Water Conductivity"
        :itemValue="props.data.waterConductivity.toString()"
      >
        <ElectricityIcon class="w-4 h-4" />
      </PlantStatusItem>
      <PlantStatusItem itemName="Temperature (°C)" :itemValue="props.data.temperature.toString()">
        <TemperatureIcon class="w-4 h-4" />
      </PlantStatusItem>
      <PlantStatusItem itemName="Last Updated" :itemValue="props.data.lastUpdated">
        <DownloadIcon class="w-4 h-4" />
      </PlantStatusItem>
    </div>
  </div>
</template>
