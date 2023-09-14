package main

import (
	"context"
	"fmt"
	"log"
	_ "os"
	"time"

	influxdb2 "github.com/influxdata/influxdb-client-go/v2"
	"github.com/influxdata/influxdb-client-go/v2/api/write"
)

func main() {
    token := "tRMAaKRbbvAwfLBsDC2rWleCJZwVvtLpSzFPxv9byfX5KnTOhvztkiXeUpBnVknDqNUs4GEnrzK4ImdauoN-pg=="
    url := "http://localhost:8086"
    client := influxdb2.NewClient(url, token)
    org := "ug"
    bucket := "garden"
    writeAPI := client.WriteAPIBlocking(org, bucket)
    for value := 0; value < 5; value++ {
        tags := map[string]string{
            "location": "42-Heilbronn",
            "sensor_id": "001",
        }
        fields := map[string]interface{}{
            "value": value,
            "status": "OK",
        }
        point := write.NewPoint("pH_sensor", tags, fields, time.Now())
        time.Sleep(1 * time.Second)
        if err := writeAPI.WritePoint(context.Background(), point); err != nil {
            log.Fatal(err)
        }
    }

    queryAPI := client.QueryAPI(org)
    query := `from(bucket: "garden")
                |> range(start: -40m)
                |> filter(fn: (r) => r._measurement == "pH_sensor")`

    results, err := queryAPI.Query(context.Background(), query)
    if err != nil {
        log.Fatal(err)
    }
    for results.Next() {
        check := results.Record().ValueByKey("_field")
        if check == "value" {
            fmt.Printf("pH-Value: %v at %s\n", results.Record().Value(), results.Record().Time())
        } else if check == "status" {
            fmt.Printf("Everything is: %s\n", results.Record().Value())
        }
    }
    if err := results.Err(); err != nil {
        log.Fatal(err)
    }
}
