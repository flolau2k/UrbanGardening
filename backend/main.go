package main

import (
	_ "context"
	"fmt"
	_ "log"
	_ "os"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
	influxdb2 "github.com/influxdata/influxdb-client-go/v2"
)

const (
    token = "tRMAaKRbbvAwfLBsDC2rWleCJZwVvtLpSzFPxv9byfX5KnTOhvztkiXeUpBnVknDqNUs4GEnrzK4ImdauoN-pg=="
    url = "http://localhost:8086"
    org = "ug"
)

func main() {
	r := gin.Default()
	r.Use(cors.Default())

	r.GET("/data", func(c *gin.Context) {
		bucketName := c.DefaultQuery("bucket", "garden")
		startTime := c.DefaultQuery("time", "15m")
		measurement := c.DefaultQuery("measurement", "pH_Sensor")

		client := influxdb2.NewClient(url, token)
		queryAPI := client.QueryAPI(org)

		query := fmt.Sprintf(`from(bucket: "%s")
					|> range(start: -%s)
					|> filter(fn: (r) => r._measurement == "%s")`,
				bucketName, startTime, measurement)

		result, err := queryAPI.Query(c, query)
		if err != nil {
			c.JSON(500, gin.H{"error": "Failed to query InfluxDB"})
		}
		 var data []interface{}
		 for result.Next() {
			record := result.Record()
			values := record.Values()
			data = append(data, values)
		 }

		 if result.Err() != nil {
			 c.JSON(500, gin.H{"error": fmt.Sprintf("Failed to read data: %s", result.Err().Error())})
		 }

		 c.JSON(200, data)
	})


    // results, err := queryAPI.Query(context.Background(), query)
    // if err != nil {
    //     log.Fatal(err)
    // }
    // for results.Next() {
    //     check := results.Record().ValueByKey("_field")
    //     if check == "value" {
    //         fmt.Printf("pH-Value: %v at %s\n", results.Record().Value(), results.Record().Time())
    //     } else if check == "status" {
    //         fmt.Printf("Everything is: %s\n", results.Record().Value())
    //     }
    // }
    // if err := results.Err(); err != nil {
    //     log.Fatal(err)
    // }
}
