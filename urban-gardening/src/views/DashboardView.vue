<script setup lang="ts" type="module">
  import StatusComponent from '../components/StatusComponent.vue';
  import CameraComponent from '../components/CameraComponent.vue';
  import { StatusData } from '../../types/Status';
  import { ChartOptions, ChartData } from 'chart.js'
  import ChartComponent from '../components/ChartComponent.vue';
  import {InfluxDB} from '@influxdata/influxdb-client-browser'
  import { DropDownData } from '../../types/DropDownData';
  import { onMounted, ref, reactive } from 'vue';

  const mockDataPlantStatus: StatusData = {kindOfPlants: 1, lastUpdated: new Date(), ph: 3, temperature: 36, waterConductivity: 2, waterLevel: 5}
  const data = reactive({
    xValues: [],
    yValues: []
  });

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

const getChartData = (tmpY: Array<number>, tmpX: Array<number>): ChartData => {
  return {
  labels: tmpX,
  datasets: [
    {
      label: 'Monthly Sales',
      backgroundColor: 'rgb(45 212 191)',
      borderColor: 'rgba(75,192,192,1)',
      data: tmpY,
      fill: false,
    }
  ]
  };
};

const mockChartData = ref<ChartData>(getChartData([], []));

const timeChange = (e: DropDownData): void => {
  //
}

const dataChange = (e: DropDownData): void => {
  //
}

const token = "tRMAaKRbbvAwfLBsDC2rWleCJZwVvtLpSzFPxv9byfX5KnTOhvztkiXeUpBnVknDqNUs4GEnrzK4ImdauoN-pg=="
const url = 'http://localhost:8086'
const org = `ug`
const currentTime = new Date()


const createQuery = (bucketName: string, dataFilter: string, startTime: string): string => {
    const queryRange = `start: -${startTime}`
    return `from(bucket: "${bucketName}")
     |> range(${queryRange})
     |> filter(fn: (r) => r._measurement == "${dataFilter}")`
}

const establishConnection = (token: string, url: string) => {

    const client = new InfluxDB({url, token})
    return client
}

onMounted(() => {
    updatePlant()
    console.log(data.yValues)
    console.log(data.xValues)
})

const updatePlant = (): void => {

    const tmpY: Array<number> = []
    const tmpX: Array<number> = []

    const client = establishConnection(token, url)
    const fluxQuery = createQuery("garden", "pH_Sensor", "5m")
    const queryClient = client.getQueryApi(org)

    queryClient.queryRows(fluxQuery, {
      next: (row: any, tableMeta: any) => {
        const tableObject = tableMeta.toObject(row)
        const d = new Date(tableObject["_time"])
        tmpY.push(Number(tableObject["_value"]))
        tmpX.push(d.getTime() - currentTime.getTime())
      },
      error: (error: any) => {
        console.error('\nError', error)
      },
      complete: () => {
        // console.log('\nSuccess');
        mockChartData.value = getChartData(tmpY, tmpX)
        // console.log(mockChartData.value)
      },
    })
}

</script>

<template>
  <div class="w-full">
    <div class="flex w-full p-10 ">
      <div class="flex-grow">
        <StatusComponent :data="mockDataPlantStatus" />
      </div>
      <div>
        <CameraComponent/>
      </div>
    </div>
    <div class="w-1/2 h-2/3">
      <ChartComponent
        @time="timeChange"
        @data-type="dataChange"
        @update="updatePlant"
        type="line"
        :dataSet="mockChartData"
        :options="mockChartOptions"
      />
    </div>
  </div>
</template>
