<script setup lang="ts">
import { ref, onUnmounted, defineProps, watchEffect } from 'vue'
import {
  Chart,
  LineController,
  BarController,
  PieController,
  CategoryScale,
  LinearScale,
  Title,
  Legend,
  ChartData,
  ChartOptions,
  PointElement,
  ChartType,
  LineElement,
  BarElement,
  Filler,
  Tooltip
} from 'chart.js'
import CustomButton from './CustomButton.vue'

Chart.register(
  LineController,
  BarController,
  PieController,
  CategoryScale,
  LinearScale,
  Title,
  Legend,
  PointElement,
  LineElement,
  BarElement,
  Filler,
  Tooltip
)

const chartElement = ref<HTMLCanvasElement | null>(null)
const emit = defineEmits(['update'])
let chartInstance: Chart | null = null

const props = defineProps({
  type: {
    type: String as () => ChartType,
    required: true
  },
  dataSet: {
    type: Object as () => ChartData,
    required: true
  },
  options: Object as () => ChartOptions | null
})

watchEffect(async () => {
  if (chartElement.value) {
    const ctx = chartElement.value.getContext('2d')
    if (chartInstance) {
      chartInstance.destroy()
    }
    chartInstance = new Chart(ctx, {
      type: props.type,
      data: props.dataSet,
      options: props.options
    })
  }
})

onUnmounted(() => {
  if (chartInstance) {
    chartInstance.destroy()
  }
})

const emitUpdate = (): void => {
  emit('update')
}
</script>

<template>
  <div class="bg-white p-4 rounded-lg">
    <!-- TODO: REMOVE -->
    <div class="flex justify-end pb-5">
      <div>
        <CustomButton @custom-click="emitUpdate" button-name="Update" />
      </div>
    </div>
    <canvas class="z-30" ref="chartElement"></canvas>
  </div>
</template>
