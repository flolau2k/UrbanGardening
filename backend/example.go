package main

import (
	"time"

	"github.com/gin-gonic/gin"
)

func test() {
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
			"status": "success",
			"timestamp": time.Now().Unix(),
			"details": gin.H{
				"version": "1.0.0",
				"description": "Sample API",
			},
			"list": []string{"item1", "item2", "item3"},
		})
	})
	r.Run()
}
