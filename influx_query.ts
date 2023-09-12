const {InfluxDB, Point} = require('@influxdata/influxdb-client')

const token = "6ocd2WQTM6KhjF6-BJEEEiZzR0ZwuDYRYafRxpVgQoatq8tub9jIpMDSJ2_k_i0r7SEYH7c3x1pls6cxwf191w=="
const url = 'http://localhost:8086'

let org = `iot`

const establishConnection = (token: string, url: string) => {

    const client = new InfluxDB({url, token})
    return client
}

const createQuery = (bucketName: string, startTime: string, dataFilter: string): string => {
    const queryRange = `start: -${startTime}m`
    return `from(bucket: "${bucketName}")
     |> range(${queryRange})
     |> filter(fn: (r) => r._measurement == "${dataFilter}")`
}

const fluxQuery = createQuery("urban", "100", "measurement1")
const client = establishConnection(token, url)
const currentTime = new Date()

let queryClient = client.getQueryApi(org)

queryClient.queryRows(fluxQuery, {
  next: (row: any, tableMeta: any) => {
    const tableObject = tableMeta.toObject(row)
    // tableObject is a dictionary
    console.log(tableObject["_value"])
    console.log(tableObject["_field"])
    const d = new Date(tableObject["_time"])
    console.log(d.getTime() - currentTime.getTime())
    console.log(tableObject)
  },
  error: (error: any) => {
    console.error('\nError', error)
  },
  complete: () => {
    console.log('\nSuccess')
  },
})
