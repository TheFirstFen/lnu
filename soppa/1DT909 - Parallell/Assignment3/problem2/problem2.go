package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"strconv"
	"strings"
)

type Booking struct {
	CustName  string `json:"cust_name"`
	CustPhone string `json:"cust_phone"`
	DateFrom  string `json:"datefrom"`
	DateTo    string `json:"dateto"`
	RoomNr    int    `json:"room_nr"`
}

const basURL = "http://localhost:3000/bookings"

func CreateBooking(booking Booking) (bool, error) {
	bookingJSON, err := json.Marshal(booking)
	if err != nil {
		return false, err
	}

	req, err := http.NewRequest(http.MethodPut, fmt.Sprintf("%s/%d", basURL, booking.RoomNr), bytes.NewBuffer(bookingJSON))
	if err != nil {
		return false, err
	}

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return false, err
	}
	defer resp.Body.Close()

	return resp.StatusCode == http.StatusCreated, nil
}

func GetBooking(id int) (bool, error) {

	resp, err := http.Get(fmt.Sprintf("%s/%d", basURL, id))
	if err != nil {
		return false, err
	}
	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return false, err
	}
	fmt.Println(string(body))

	return resp.StatusCode == 200, nil
}

func DelBooking(id int) (bool, error) {
	resp, err := http.NewRequest(http.MethodDelete, fmt.Sprintf("%s/%d", basURL, id), nil)
	if err != nil {

		return false, err
	}
	body, err := http.DefaultClient.Do(resp)
	if err != nil {

		return false, err
	}
	defer body.Body.Close()

	return body.StatusCode == 200, nil

}

func UpdateBooking(id int, booking Booking) (bool, error) {
	bookingJSON, err := json.Marshal(booking)
	if err != nil {
		return false, err
	}

	req, err := http.NewRequest("UPDATE", fmt.Sprintf("%s/%d", basURL, id), bytes.NewBuffer(bookingJSON))
	if err != nil {
		return false, err
	}

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return false, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return false, fmt.Errorf("failed to update booking, status code: %d", resp.StatusCode)
	}

	return true, nil
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for {
		fmt.Println("Choose an action:")
		fmt.Println("1: Create Booking")
		fmt.Println("2: Update Booking")
		fmt.Println("3: Delete Booking")
		fmt.Println("4: Get booking from id")
		fmt.Println("5: Exit")
		fmt.Print("Enter choice: ")

		scanner.Scan()
		choice := scanner.Text()
		choice = strings.TrimSpace(choice)
		option, err := strconv.Atoi(choice)
		if err != nil {
			fmt.Println("Please enter a valid number")
			continue
		}

		switch option {
		case 1:
			createBookingMenu()
		case 2:
			updateBookingMenu()
		case 3:
			deleteBookingMenu()
		case 4:
			getBookingMenu()
		case 5:
			fmt.Println("Exiting...")
			return
		default:
			fmt.Println("Invalid choice, please try again.")
		}
	}
}

func createBookingMenu() {
	scanner := bufio.NewScanner(os.Stdin)
	booking := Booking{}

	fmt.Print("Enter customer name: ")
	scanner.Scan()
	booking.CustName = scanner.Text()

	fmt.Print("Enter customer phone: ")
	scanner.Scan()
	booking.CustPhone = scanner.Text()

	fmt.Print("Enter booking start date (YYYY-MM-DD): ")
	scanner.Scan()
	booking.DateFrom = scanner.Text()

	fmt.Print("Enter booking end date (YYYY-MM-DD): ")
	scanner.Scan()
	booking.DateTo = scanner.Text()

	fmt.Print("Enter room number: ")
	scanner.Scan()
	roomNr, _ := strconv.Atoi(scanner.Text())

	booking.RoomNr = roomNr

	b, err := CreateBooking(booking)
	if !b {
		fmt.Println("Error creating booking:", err)
	} else {
		fmt.Println("Booking successfully created!")
	}
}

func updateBookingMenu() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("Enter id to update: ")
	scanner.Scan()
	id, _ := strconv.Atoi(scanner.Text())

	fmt.Println("Updating booking:")
	b, err := GetBooking(id)
	if !b {
		fmt.Println("Error finding booking:", err)
	}

	booking := Booking{}

	fmt.Print("Enter customer name: ")
	scanner.Scan()
	booking.CustName = scanner.Text()

	fmt.Print("Enter customer phone: ")
	scanner.Scan()
	booking.CustPhone = scanner.Text()

	fmt.Print("Enter booking start date (YYYY-MM-DD): ")
	scanner.Scan()
	booking.DateFrom = scanner.Text()

	fmt.Print("Enter booking end date (YYYY-MM-DD): ")
	scanner.Scan()
	booking.DateTo = scanner.Text()

	fmt.Print("Enter room number: ")
	scanner.Scan()
	roomNr, _ := strconv.Atoi(scanner.Text())

	booking.RoomNr = roomNr

	b, err = UpdateBooking(id, booking)
	if !b {
		fmt.Println("Error Updating booking:", err)
	} else {
		fmt.Println("Booking successfully Updated!")
	}
}

func deleteBookingMenu() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("Enter id to delete: ")
	scanner.Scan()
	id, _ := strconv.Atoi(scanner.Text())

	b, err := DelBooking(id)
	if !b {
		fmt.Println("Error deleting booking:", err)
	} else {
		fmt.Println("Booking successfully deleted!")
	}
}

func getBookingMenu() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("Enter id to get info about: ")
	scanner.Scan()
	id, _ := strconv.Atoi(scanner.Text())

	b, err := GetBooking(id)
	if !b {
		fmt.Println("Error getting booking:", err)
	}
}
