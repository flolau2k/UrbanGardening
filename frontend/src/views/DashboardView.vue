<script setup lang="ts" type="module">
import StatusComponent from '../components/StatusComponent.vue'
import CameraComponent from '../components/CameraComponent.vue'
import type { StatusData } from '../../types/Status'
import type { ChartOptions, ChartData, ChartType } from 'chart.js'
import ChartComponent from '../components/ChartComponent.vue'
import type { DropDownData } from '../../types/DropDownData'
import { onMounted, ref } from 'vue'
import ConfigCard from '../components/ConfigCard.vue'
import axiosInstance from '../api/axiosInstance'


const mockDataPlantStatus: StatusData = {
  kindOfPlants: 1,
  lastUpdated: new Date(),
  ph: 3,
  temperature: 36,
  waterConductivity: 2,
  waterLevel: 5
}

const graphType = ref<ChartType>('line')
const dataType = ref<DropDownData>()
const plantType = ref<DropDownData>()
const timeRange = ref<DropDownData>()

const chartOptions: ChartOptions = {
  responsive: true,
  scales: {
    x: {
      title: {
        display: true,
        text: 'Timestamp'
      }
    }
  },
  plugins: {
    legend: {
      display: true,
      position: 'top'
    },
    title: {
      display: true,
      text: 'A graph ¯\\_(ツ)_/¯'
    }
  }
}

const updateChartData = (yValues: Array<number>, xValues: Array<number>): ChartData => {
  return {
    labels: xValues,
    datasets: [
      {
        label: 'Dataset',
        backgroundColor: 'rgb(45 212 191)',
        borderColor: 'rgba(75,192,192,1)',
        data: yValues,
        fill: false
      }
    ]
  }
}

const chartData = ref<ChartData>(updateChartData([], []))

const fetchChartData = async () => {
  // Check the inputs/params before making request
  if (!timeRange.value || !dataType.value) {
    alert('Please select a time range and data type!')
    return ;
  }
  try {
    const response = await axiosInstance.get('/api/chart-data', {
      params: {
        bucketName: 'garden',
        startTime: timeRange.value.value,
        measurement: dataType.value.value
      }
    })
    // Update the chart component with new data recieved from server
    chartData.value = updateChartData(response.data.yValues, response.data.xValues)
  } catch (error) {
    console.error('Error fetching data:', error)
    alert("Error when fetching data! Check the console for more information.");
  }
}

// const fetchPlantData = (): void => {
//   const tmpY: Array<number> = []
//   const tmpX: Array<number> = []

//   const client = establishConnection(token, url)
//   const fluxQuery = createQuery('garden', 'pH_Sensor', '5m')
//   const queryClient = client.getQueryApi(org)

//   queryClient.queryRows(fluxQuery, {
//     next: (row: any, tableMeta: any) => {
//       const tableObject = tableMeta.toObject(row)
//       const d = new Date(tableObject['_time'])
//       tmpY.push(Number(tableObject['_value']))
//       tmpX.push(d.getTime() - currentTime.getTime())
//     },
//     error: (error: any) => {
//       console.error('\nError', error)
//     },
//     complete: () => {
//       // console.log('\nSuccess');
//       mockChartData.value = updateChartData(tmpY, tmpX)
//       // console.log(mockChartData.value)
//     }
//   })
// }

const isChartType = (value: string): value is ChartType => {
  return ['line', 'bar'].includes(value)
}

const timeChange = (item: DropDownData): void => {
  timeRange.value = item
}

const dataTypeChange = (item: DropDownData): void => {
  dataType.value = item
}

const graphTypeChange = (item: DropDownData): void => {
  if (isChartType(item.value)){
    graphType.value = item.value as ChartType;
    // Set new graph type in localstorage
    localStorage.setItem("graphType", item.value);
  } 
  else alert('Invalid chart type!')
}

const plantTypeChange = (item: DropDownData): void => {
  plantType.value = item
}

onMounted(() => {
  // Check if there is agraph type stored in localstorage
  const storedGraphType = localStorage.getItem('graphType');
  if (storedGraphType) {
    graphType.value = storedGraphType as ChartType
  }
})

</script>

<template>
  <div class="w-full">
    <div class="flex justify-between w-full p-10">
      <ConfigCard
        @selected-plant-type="plantTypeChange"
        @selected-data-type="dataTypeChange"
        @selected-graph-type="graphTypeChange"
        @selected-time-data="timeChange"
        @emit-data-fetch-click="fetchChartData"
      />
      <StatusComponent :data="mockDataPlantStatus" />
      <CameraComponent />
    </div>
    <div class="flex justify-center">
      <div class="w-2/3 h-2/3">
        <ChartComponent :type="graphType" :dataSet="chartData" :options="chartOptions" />
      </div>
    </div>
  </div>
</template>
