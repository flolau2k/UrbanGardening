var _a = require('@influxdata/influxdb-client'), InfluxDB = _a.InfluxDB, Point = _a.Point;
var token = "6ocd2WQTM6KhjF6-BJEEEiZzR0ZwuDYRYafRxpVgQoatq8tub9jIpMDSJ2_k_i0r7SEYH7c3x1pls6cxwf191w==";
var url = 'http://localhost:8086';
// const client = new InfluxDB({url, token})
var org = "iot";
// let bucket = `urban`
// let writeClient = client.getWriteApi(org, bucket, 'ns')
// 
// for (let i = 0; i < 5; i++) {
//   let point = new Point('measurement1')
//     .tag('tagname1', 'tagvalue1')
//     .intField('field1', i)
// 
//   void setTimeout(() => {
//     writeClient.writePoint(point)
//   }, i * 1000) // separate points by 1 second
// 
//   void setTimeout(() => {
//     writeClient.flush()
//   }, 5000)
// }
var establishConnection = function (token, url) {
    var client = new InfluxDB({ url: url, token: token });
    return client;
};
var createQuery = function (bucketName, startTime, dataFilter) {
    var queryRange = "start: -".concat(startTime, "m");
    return "from(bucket: \"".concat(bucketName, "\")\n     |> range(").concat(queryRange, ")\n     |> filter(fn: (r) => r._measurement == \"").concat(dataFilter, "\")");
};
var fluxQuery = createQuery("urban", "100", "measurement1");
var client = establishConnection(token, url);
var currentTime = new Date();
// 
// const bucketName = "urban"
// const startTime = "100"
// const queryRange = `start: -${startTime}m`
// const dataFilter = "measurement1"
var queryClient = client.getQueryApi(org);
queryClient.queryRows(fluxQuery, {
    next: function (row, tableMeta) {
        var tableObject = tableMeta.toObject(row);
        console.log(tableObject["_value"]);
        console.log(tableObject["_field"]);
        var d = new Date(tableObject["_time"]);
        console.log(d.getTime() - currentTime.getTime());
        console.log(tableObject);
    },
    error: function (error) {
        console.error('\nError', error);
    },
    complete: function () {
        console.log('\nSuccess');
    }
});
