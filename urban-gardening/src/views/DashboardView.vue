<script setup lang="ts">
  import StatusComponent from '../components/StatusComponent.vue';
  import CameraComponent from '../components/CameraComponent.vue';
  import { StatusData } from '../../types/Status';
  import { ChartOptions, ChartData } from 'chart.js'
  import ChartComponent from '../components/ChartComponent.vue';

  const mockDataPlantStatus: StatusData = {kindOfPlants: 1, lastUpdated: new Date(), ph: 3, temperature: 36, waterConductivity: 2, waterLevel: 5}

  const mockChartOptions: ChartOptions = {
  responsive: true,
  scales: {
    y: {
      beginAtZero: true,
      title: {
        display: true,
        text: "Number of sales"
      },
    },
    x: {
      title: {
        display: true,
        text: 'Month'
      }
    }
  },
  plugins: {
    legend: {
      display: true,
      position: 'top',
    },
    title: {
      display: true,
      text: 'Monthly Sales for Product X'
    },
  }
};

const mockChartData: ChartData = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
  datasets: [
    {
      label: 'Monthly Sales',
      backgroundColor: 'rgb(45 212 191)',
      borderColor: 'rgba(75,192,192,1)',
      data: [120, 150, 170, 140, 180, 210, 220, 200, 240, 250, 230, 260],
      fill: false,
    }
  ]
};

const updatePlant = (): void => {
  // call api here and assign data
}

</script>

<template>
  <div class="w-full">
    <div class="flex w-full p-10 ">
      <div class="flex-grow">
        <StatusComponent @updatePlant="updatePlant" :data="mockDataPlantStatus" />
      </div>
      <div>
        <CameraComponent/>
      </div>
    </div>
    <div class="w-1/2 h-2/3">
      <ChartComponent
        type="line"
        :dataSet="mockChartData"
        :options="mockChartOptions"
      />
    </div>
    <div class="mt-20 w-1/2 h-2/3">
      <ChartComponent
        type="bar"
        :dataSet="mockChartData"
        :options="mockChartOptions"
      />
    </div>
  </div>
</template>
