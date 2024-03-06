package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

type Student struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Age   int    `json:"age"`
	Grade string `json:"grade"`
}

const (
	DBHost     = "localhost"
	DBPort     = "3306"
	DBUser     = "root"
	DBPassword = "3q1t6IBJ*"
	DBName     = "students_db"
)

var db *sql.DB

func initDB() {
	dataSourceName := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s", DBUser, DBPassword, DBHost, DBPort, DBName)
	var err error
	db, err = sql.Open("mysql", dataSourceName)
	if err != nil {
		log.Fatal("Error connecting to database:", err)
	}
}

func closeDB() {
	db.Close()
}

func CreateStudent(w http.ResponseWriter, r *http.Request) {
	var student Student
	err := json.NewDecoder(r.Body).Decode(&student)
	if err != nil {
		http.Error(w, "Invalid student data", http.StatusBadRequest)
		return
	}

	result, err := db.Exec("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", student.Name, student.Age, student.Grade)
	if err != nil {
		http.Error(w, "Error creating student", http.StatusInternalServerError)
		return
	}

	studentID, _ := result.LastInsertId()
	student.ID = int(studentID)

	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(student)
}

func GetStudent(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	id := params["id"]

	var student Student
	err := db.QueryRow("SELECT id, name, age, grade FROM students WHERE id = ?", id).Scan(&student.ID, &student.Name, &student.Age, &student.Grade)
	if err != nil {
		if err == sql.ErrNoRows {
			http.Error(w, "Student not found", http.StatusNotFound)
		} else {
			http.Error(w, "Error retrieving student", http.StatusInternalServerError)
		}
		return
	}

	json.NewEncoder(w).Encode(student)
}

func UpdateStudent(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	id := params["id"]

	var student Student
	err := json.NewDecoder(r.Body).Decode(&student)
	if err != nil {
		http.Error(w, "Invalid student data", http.StatusBadRequest)
		return
	}

	_, err = db.Exec("UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?", student.Name, student.Age, student.Grade, id)
	if err != nil {
		http.Error(w, "Error updating student", http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusOK)
}

func DeleteStudent(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	id := params["id"]

	_, err := db.Exec("DELETE FROM students WHERE id = ?", id)
	if err != nil {
		http.Error(w, "Error deleting student", http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusOK)
}

func main() {
	initDB()
	defer closeDB()

	router := mux.NewRouter()

	router.HandleFunc("/students", CreateStudent).Methods("POST")
	router.HandleFunc("/students/{id}", GetStudent).Methods("GET")
	router.HandleFunc("/students/{id}", UpdateStudent).Methods("PUT")
	router.HandleFunc("/students/{id}", DeleteStudent).Methods("DELETE")

	port := os.Getenv("PORT")
	if port == "" {
		port = "3000"
	}

	log.Printf("Server running on port %s\n", port)
	log.Fatal(http.ListenAndServe(":"+port, router))
}
