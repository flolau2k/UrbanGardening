<script setup lang="ts" type="module">
import StatusComponent from '../components/StatusComponent.vue'
import CameraComponent from '../components/CameraComponent.vue'
import { StatusData } from '../../types/Status'
import { ChartOptions, ChartData, ChartType } from 'chart.js'
import ChartComponent from '../components/ChartComponent.vue'
import { InfluxDB } from '@influxdata/influxdb-client-browser'
import { DropDownData } from '../../types/DropDownData'
import { onMounted, ref } from 'vue'
import ConfigCard from '../components/ConfigCard.vue'

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

const token =
  'tRMAaKRbbvAwfLBsDC2rWleCJZwVvtLpSzFPxv9byfX5KnTOhvztkiXeUpBnVknDqNUs4GEnrzK4ImdauoN-pg=='
const url = 'http://localhost:8086'
const org = `ug`
const currentTime = new Date()

const mockChartOptions: ChartOptions = {
  responsive: true,
  scales: {
    x: {
      title: {
        display: true,
        text: 'Value'
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
      text: 'Graph showing data :)'
    }
  }
}

const getChartData = (tmpY: Array<number>, tmpX: Array<number>): ChartData => {
  return {
    labels: tmpX,
    datasets: [
      {
        label: 'Dataset',
        backgroundColor: 'rgb(45 212 191)',
        borderColor: 'rgba(75,192,192,1)',
        data: tmpY,
        fill: false
      }
    ]
  }
}

const mockChartData = ref<ChartData>(getChartData([], []))

const createQuery = (bucketName: string, dataFilter: string, startTime: string): string => {
  const queryRange = `start: -${startTime}`
  return `from(bucket: "${bucketName}")
     |> range(${queryRange})
     |> filter(fn: (r) => r._measurement == "${dataFilter}")`
}

const establishConnection = (token: string, url: string) => {
  const client = new InfluxDB({ url, token })
  return client
}

onMounted(() => {
  updatePlant()
})

const updatePlant = (): void => {
  const tmpY: Array<number> = []
  const tmpX: Array<number> = []

  const client = establishConnection(token, url)
  const fluxQuery = createQuery('garden', 'pH_Sensor', '5m')
  const queryClient = client.getQueryApi(org)

  queryClient.queryRows(fluxQuery, {
    next: (row: any, tableMeta: any) => {
      const tableObject = tableMeta.toObject(row)
      const d = new Date(tableObject['_time'])
      tmpY.push(Number(tableObject['_value']))
      tmpX.push(d.getTime() - currentTime.getTime())
    },
    error: (error: any) => {
      console.error('\nError', error)
    },
    complete: () => {
      // console.log('\nSuccess');
      mockChartData.value = getChartData(tmpY, tmpX)
      // console.log(mockChartData.value)
    }
  })
}

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
  if (isChartType(item.value)) graphType.value = item.value as ChartType
  else alert('Invalid chart type!')
}

const plantTypeChange = (item: DropDownData): void => {
  plantType.value = item
}
</script>

<template>
  <div class="w-full">
    <div class="flex justify-between w-full p-10">
      <ConfigCard
        @selected-plant-type="plantTypeChange"
        @selected-data-type="dataTypeChange"
        @selected-graph-type="graphTypeChange"
        @selected-time-data="timeChange"
        @emit-data-fetch-click="updatePlant"
      />
      <StatusComponent :data="mockDataPlantStatus" />
      <CameraComponent />
    </div>
    <div class="w-1/2 h-2/3">
      <ChartComponent
        @update="updatePlant"
        :type="graphType"
        :dataSet="mockChartData"
        :options="mockChartOptions"
      />
    </div>
  </div>
</template>
