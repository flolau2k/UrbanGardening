<script setup lang="ts">
import { ref, onUnmounted, watchEffect } from 'vue'
import type { ChartData, ChartOptions, ChartType } from 'chart.js';
import {
  Chart,
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
} from 'chart.js'

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
    if (ctx) {
    chartInstance = new Chart(ctx, {
      type: props.type,
      data: props.dataSet,
      options: props.options || undefined
    })
    }
  }
})

onUnmounted(() => {
  if (chartInstance) {
    chartInstance.destroy()
  }
})
</script>

<template>
  <div class="bg-white p-4 rounded-lg">
    <canvas class="z-30" ref="chartElement"></canvas>
  </div>
</template>
