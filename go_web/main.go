package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

// Task представляю структуру задачи
type Task struct {
	ID     int    `json:"id"`
	Title  string `json:"title"`
	Status bool   `json:"status"`
}

var tasks = []Task{
	{ID: 1, Title: "Купить молоко", Status: true},
	{ID: 2, Title: "Выгулять собаку", Status: false},
	{ID: 3, Title: "Сделать ДЗ", Status: false},
}

func getTasks(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, tasks)
}

func postTask(c *gin.Context) {
	var newTask Task
	if err := c.BindJSON(&newTask); err != nil {
		c.IndentedJSON(http.StatusBadRequest, "bad_request")
		return
	}
	tasks = append(tasks, newTask)
	c.IndentedJSON(http.StatusCreated, newTask)
}
func updateTask(c *gin.Context) {
	// Парсим JSON-данные с новыми значениями для задачи
	var updatedTask Task
	if err := c.BindJSON(&updatedTask); err != nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"error": "bad_request"})
		return
	}

	// Ищем задачу с указанным названием в списке задач
	for i, task := range tasks {
		if task.Title == updatedTask.Title {
			// Обновляем значение статуса задачи
			tasks[i].Status = updatedTask.Status
			c.IndentedJSON(http.StatusOK, tasks[i])
			return
		}
	}

	// Если задача с указанным названием не найдена, возвращаем ошибку 404 Not Found
	c.IndentedJSON(http.StatusNotFound, gin.H{"error": "task_not_found"})
}

func deleteTask(c *gin.Context) {
	var deleteTask struct {
		Title string `json:"title"`
	}
	if err := c.BindJSON(&deleteTask); err != nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"error": "bad_request"})
		return
	}

	for i, task := range tasks {
		if task.Title == deleteTask.Title {
			tasks = append(tasks[:i], tasks[i+1:]...)
			c.IndentedJSON(http.StatusOK, gin.H{"message": "task_deleted"})
			return
		}
	}

	c.IndentedJSON(http.StatusNotFound, gin.H{"error": "task_not_found"})
}

func main() {
	a := 11
	fmt.Println(a)
	router := gin.Default()
	router.GET("/tasks", getTasks)
	router.POST("/tasks", postTask)
	router.PUT("/tasks", updateTask)
	router.DELETE("/tasks", deleteTask)
	router.GET("/", func(c *gin.Context) {
		c.String(http.StatusOK, "Привет!")
	})
	router.Run("localhost:8080")
}
