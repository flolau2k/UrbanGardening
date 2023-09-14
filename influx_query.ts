const {InfluxDB, Point} = require('@influxdata/influxdb-client')

const token = "tRMAaKRbbvAwfLBsDC2rWleCJZwVvtLpSzFPxv9byfX5KnTOhvztkiXeUpBnVknDqNUs4GEnrzK4ImdauoN-pg=="
const url = 'http://localhost:8086'
let org = `ug`

const establishConnection = (token: string, url: string) => {

    const client = new InfluxDB({url, token})
    return client
}

const createQuery = (bucketName: string, dataFilter: string, startTime: string): string => {
    const queryRange = `start: -${startTime}`
    return `from(bucket: "${bucketName}")
     |> range(${queryRange})
     |> filter(fn: (r) => r._measurement == "${dataFilter}")`
}

const fluxQuery = createQuery("garden", "pH_Sensor", "15m")
const client = establishConnection(token, url)
const currentTime = new Date()

let queryClient = client.getQueryApi(org)

queryClient.queryRows(fluxQuery, {
  next: (row: any, tableMeta: any) => {
    const tableObject = tableMeta.toObject(row)
    console.log(tableObject["_value"]) // value for the y axis
    // console.log(tableObject["_measurement"])
    const d = new Date(tableObject["_time"])
    console.log(d.getTime() - currentTime.getTime()) // value for the x axis
    console.log(tableObject)
  },
  error: (error: any) => {
    console.error('\nError', error)
  },
  complete: () => {
    console.log('\nSuccess')
  },
})
