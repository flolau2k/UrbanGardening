var _a = require('@influxdata/influxdb-client'), InfluxDB = _a.InfluxDB, Point = _a.Point;
var token = "tRMAaKRbbvAwfLBsDC2rWleCJZwVvtLpSzFPxv9byfX5KnTOhvztkiXeUpBnVknDqNUs4GEnrzK4ImdauoN-pg==";
var url = 'http://localhost:8086';
var org = "ug";
var establishConnection = function (token, url) {
    var client = new InfluxDB({ url: url, token: token });
    return client;
};
var createQuery = function (bucketName, dataFilter, startTime) {
    var queryRange = "start: -".concat(startTime);
    return "from(bucket: \"".concat(bucketName, "\")\n     |> range(").concat(queryRange, ")\n     |> filter(fn: (r) => r._measurement == \"").concat(dataFilter, "\")");
};
var fluxQuery = createQuery("garden", "pH_Sensor", "15m");
var client = establishConnection(token, url);
var currentTime = new Date();
var queryClient = client.getQueryApi(org);
queryClient.queryRows(fluxQuery, {
    next: function (row, tableMeta) {
        var tableObject = tableMeta.toObject(row);
        console.log(tableObject["_value"]); // value for the y axis
        console.log(tableObject["_measurement"]); // value for the y axis
        // console.log(tableObject["_field"])
        var d = new Date(tableObject["_time"]);
        console.log(d.getTime() - currentTime.getTime()); // value for the x axis
        console.log(tableObject);
    },
    error: function (error) {
        console.error('\nError', error);
    },
    complete: function () {
        console.log('\nSuccess');
    }
});
