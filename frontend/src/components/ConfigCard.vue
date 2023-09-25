<script setup lang="ts">
import DropDown from './DropDown.vue'
import SettingsIcon from './icons/SettingsIcon.vue'
import type { DropDownData } from '../../types/DropDownData'
import { onMounted, ref } from 'vue'
import CustomButton from './CustomButton.vue'

const emit = defineEmits<{
  (event: 'selectedPlantType', selection: DropDownData): void
  (event: 'selectedGraphType', selection: DropDownData): void
  (event: 'selectedTimeData', selection: DropDownData): void
  (event: 'selectedDataType', selection: DropDownData): void
  (event: 'emitDataFetchClick'): void
}>()

const plantType = ref<DropDownData[]>([])
const graphType = ref<DropDownData[]>([])
const timeData = ref<DropDownData[]>([])
const dataType = ref<DropDownData[]>([])

const emitSelectedPlantType = (selection: DropDownData): void => {
  emit('selectedPlantType', selection)
}

const emitSelectedGraphType = (selection: DropDownData): void => {
  emit('selectedGraphType', selection)
}

const emitSelectedTimeData = (selection: DropDownData): void => {
  emit('selectedTimeData', selection)
}

const emitSelectedDataType = (selection: DropDownData): void => {
  emit('selectedDataType', selection)
}

const emitDataFetchClick = (): void => {
  emit('emitDataFetchClick')
}

const getDropdownData = async (url: string): Promise<DropDownData[]> => {
  try {
    const response = await fetch(url)
    if (!response.ok) {
      throw new Error('Failed to fetch data')
    }
    const jsonData = await response.json()
    const data: DropDownData[] = jsonData.data
    return data
  } catch (error) {
    console.error('Error fetching data:', error)
    return []
  }
}

onMounted(() => {
  getDropdownData('../../src/dropdown-data/plant-type-data.json').then((data: DropDownData[]) => {
    plantType.value = data
  })

  getDropdownData('../../src/dropdown-data/graph-type-data.json').then((data: DropDownData[]) => {
    graphType.value = data
  })

  getDropdownData('../../src/dropdown-data/time-data.json').then((data: DropDownData[]) => {
    timeData.value = data
  })
  getDropdownData('../../src/dropdown-data/data-type.json').then((data: DropDownData[]) => {
    dataType.value = data
  })
})
</script>

<template>
  <div class="bg-white w-[420px] h-[230px] p-4 rounded-lg">
    <div class="flex text-teal-500 flex-grow items-center gap-x-3">
      <div>
        <SettingsIcon class="w-10 h-10" />
      </div>
      <div class="text-2xl font-bold">Config</div>
    </div>
    <div class="grid grid-cols-2 gap-x-5 justify-center">
      <div class="col-span-1">
        <DropDown
          @selected-item="emitSelectedPlantType"
          :data="plantType"
          class="w-32 mt-2"
          dropdown-name="Plant Type"
        />
        <DropDown
          @selected-item="emitSelectedGraphType"
          :data="graphType"
          class="w-32 mt-2"
          dropdown-name="Graph Type"
        />
      </div>
      <div class="col-span-1">
        <DropDown
          @selected-item="emitSelectedTimeData"
          :data="timeData"
          class="w-32 mt-2"
          dropdown-name="Time"
        />
        <DropDown
          @selected-item="emitSelectedDataType"
          :data="dataType"
          class="w-32 mt-2"
          dropdown-name="Data Type"
        />
      </div>
    </div>
    <div class="flex justify-center pt-8">
      <div>
        <CustomButton @custom-click="emitDataFetchClick" button-name="Fetch Data" />
      </div>
    </div>
  </div>
</template>
