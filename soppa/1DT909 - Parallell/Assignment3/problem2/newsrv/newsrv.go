package main

import (
	"database/sql"
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"
	"strconv"
	"sync"

	"github.com/go-sql-driver/mysql"
)

type Booking struct {
	ID        int    `json:"id"`
	CustName  string `json:"cust_name"`
	CustPhone string `json:"cust_phone"`
	DateFrom  string `json:"datefrom"`
	DateTo    string `json:"dateto"`
	RoomNr    int    `json:"room_nr"`
}

const (
	dbUser     = "***"
	dbPassword = "***"
	dbName     = "godb"
)

var db *sql.DB
var mu sync.Mutex

func initDB() {

	cfg := mysql.Config{
		User:   dbUser,
		Passwd: dbPassword,
		DBName: dbName,
	}
	var err error
	db, err = sql.Open("mysql", cfg.FormatDSN())
	if err != nil {
		log.Fatal(err)
	}

	err = db.Ping()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Database connection established")
}

func createBooking(rw http.ResponseWriter, r *http.Request) {
	var b Booking
	err := json.NewDecoder(r.Body).Decode(&b)
	if err != nil {
		http.Error(rw, err.Error(), http.StatusBadRequest)
		return
	}

	result, err := db.Exec("INSERT INTO bookings (cust_name, cust_phone, datefrom, dateto, room_nr) VALUES (?, ?, ?, ?, ?)", b.CustName, b.CustPhone, b.DateFrom, b.DateTo, b.RoomNr)
	if err != nil {
		http.Error(rw, err.Error(), http.StatusInternalServerError)
		return
	}

	id, err := result.LastInsertId()
	if err != nil {
		http.Error(rw, err.Error(), http.StatusInternalServerError)
		return
	}
	b.ID = int(id)
	rw.WriteHeader(http.StatusCreated)
	json.NewEncoder(rw).Encode(b)
}

func getBooking(rw http.ResponseWriter, r *http.Request) {
	id := r.PathValue("key")
	intID, err := strconv.Atoi(id)
	if err != nil {
		http.Error(rw, err.Error(), http.StatusBadRequest)
		return
	}

	var b Booking
	err = db.QueryRow("SELECT id, cust_name, cust_phone, datefrom, dateto, room_nr FROM bookings WHERE id = ?", intID).Scan(&b.ID, &b.CustName, &b.CustPhone, &b.DateFrom, &b.DateTo, &b.RoomNr)
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			http.NotFound(rw, r)
		} else {
			http.Error(rw, err.Error(), http.StatusInternalServerError)
		}
		return
	}

	json.NewEncoder(rw).Encode(b)
}

func updateBooking(rw http.ResponseWriter, r *http.Request) {
	mu.Lock()
	defer mu.Unlock()
	id := r.PathValue("key")

	var updatedBooking Booking
	if err := json.NewDecoder(r.Body).Decode(&updatedBooking); err != nil {
		http.Error(rw, err.Error(), http.StatusBadRequest)
		return
	}

	intID, err := strconv.Atoi(id)
	if err != nil {
		http.Error(rw, "Invalid booking ID", http.StatusBadRequest)
		return
	}

	_, err = db.Exec("UPDATE bookings SET cust_name = ?, cust_phone = ?, datefrom = ?, dateto = ?, room_nr = ? WHERE id = ?", updatedBooking.CustName, updatedBooking.CustPhone, updatedBooking.DateFrom, updatedBooking.DateTo, updatedBooking.RoomNr, intID)
	if err != nil {
		http.Error(rw, err.Error(), http.StatusInternalServerError)
		return
	}

	rw.WriteHeader(http.StatusOK)
	json.NewEncoder(rw).Encode(updatedBooking)
}

func deleteBooking(rw http.ResponseWriter, r *http.Request) {
	mu.Lock()
	defer mu.Unlock()
	id := r.PathValue("key")

	intId, err := strconv.Atoi(id)
	if err != nil {
		http.Error(rw, "Invalid booking ID", http.StatusBadRequest)
		return
	}

	_, err = db.Exec("DELETE FROM bookings WHERE id = ?", intId)
	if err != nil {
		http.Error(rw, err.Error(), http.StatusInternalServerError)
		return
	}

	rw.WriteHeader(http.StatusOK)
}

func closeDB() {
	db.Close()
}

func main() {
	initDB()

	mux := http.NewServeMux()

	mux.HandleFunc("PUT /bookings/{key}", createBooking)
	mux.HandleFunc("GET /bookings/{key}", getBooking)
	mux.HandleFunc("DELETE /bookings/{key}", deleteBooking)
	mux.HandleFunc("UPDATE /bookings/{key}", updateBooking)

	http.ListenAndServe(":3000", mux)
	defer closeDB()
}
