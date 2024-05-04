package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	_ "strconv"
	"time"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
	influxdb2 "github.com/influxdata/influxdb-client-go/v2"
	"github.com/influxdata/influxdb-client-go/v2/api"
)

const (
	token = "tRMAaKRbbvAwfLBsDC2rWleCJZwVvtLpSzFPxv9byfX5KnTOhvztkiXeUpBnVknDqNUs4GEnrzK4ImdauoN-pg=="
	url   = "http://localhost:8086"
	org   = "ug"
)

func unfoldRequestQuery(c *gin.Context) (string, string, string) {
	bucketName := c.DefaultQuery("bucket", "garden")
	startTime := c.DefaultQuery("time", "15m")
	measurement := c.DefaultQuery("measurement", "pH_Sensor")
	return bucketName, startTime, measurement
}

func createReturnData(r *api.QueryTableResult) ([]float64, []interface{}) {
	var data []float64
	var timestamp []interface{}

	for r.Next() {
		record := r.Record()
		value := record.Value()
		data = append(data, value.(float64))
		currentTime := time.Now().UnixMilli() / 1000
		timestamp = append(timestamp, (record.Time().UnixMilli()/1000)-currentTime)
	}
	return data, timestamp
}

func handleChartData(c *gin.Context) {
	bucketName, startTime, measurement := unfoldRequestQuery(c)
	client := influxdb2.NewClient(url, token)
	queryAPI := client.QueryAPI(org)

	query := fmt.Sprintf(`from(bucket: "%s")
					|> range(start: -%s)
					|> filter(fn: (r) => r._measurement == "%s")`,
		bucketName, startTime, measurement)
	result, err := queryAPI.Query(c, query)
	if err != nil {
		c.JSON(http.StatusInternalServerError,
			gin.H{"error": "Failed to query InfluxDB"})
		return
	}
	data, timestamp := createReturnData(result)
	if result.Err() != nil {
		c.JSON(http.StatusInternalServerError,
			gin.H{"error": fmt.Sprintf("Failed to read data: %s", result.Err().Error())})
		return
	}
	c.JSON(http.StatusOK, gin.H{
		"yValues": data,
		"xValues": timestamp,
	})
}

func main() {
	gin.SetMode(gin.ReleaseMode)
	gin.DisableConsoleColor()

	f, _ := os.Create("gin.log")
	gin.DefaultWriter = io.MultiWriter(f)
	r := gin.Default()

	r.Use(cors.Default())
	r.Use(gin.Recovery())

	r.GET("/api/chart-data", handleChartData)
	r.GET("/api/example", func(ctx *gin.Context) {
		ctx.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
	})
	r.Run(":8081")
}
