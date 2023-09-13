<script setup lang="ts">
import { ref, onMounted, onUnmounted, defineProps } from 'vue';
import { Chart, LineController, BarController, PieController, CategoryScale, LinearScale, Title, Legend, ChartData, ChartOptions, PointElement, ChartType, LineElement, BarElement, Filler, Tooltip } from 'chart.js';

Chart.register(LineController, BarController, PieController, CategoryScale, LinearScale, Title, Legend, PointElement, LineElement, BarElement, Filler, Tooltip );

const props = defineProps({
  type: {
    type: String as () => ChartType,
    required: true
  },
  dataSet: {
    type: Object as () => ChartData,
    required: true
  },
  options: Object as () => ChartOptions | null,
});

const chartElement = ref<HTMLCanvasElement | null>(null);
let chartInstance: Chart | null = null;

onMounted(() => {
  if (chartElement.value) {
    const ctx = chartElement.value.getContext('2d');
    chartInstance = new Chart(ctx, {
      type: props.type,
      data: props.dataSet,
      options: props.options
    });
  }
});

onUnmounted(() => {
  if (chartInstance) {
    chartInstance.destroy();
  }
});

</script>

<template>
  <div class="bg-white p-4 rounded-lg">
    <canvas class="z-30" ref="chartElement"></canvas>
  </div>
</template>