package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"strings"
)

type Student struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Age   int    `json:"age"`
	Grade string `json:"grade"`
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var choice int

	for {
		fmt.Println("Select Operation:")
		fmt.Println("1. Create Student")
		fmt.Println("2. Get Student")
		fmt.Println("3. Update Student")
		fmt.Println("4. Delete Student")
		fmt.Println("5. Exit")

		fmt.Print("Enter your choice: ")
		_, err := fmt.Fscanf(reader, "%d\n", &choice)
		if err != nil {
			fmt.Println("Invalid input. Please enter a number.")
			continue
		}

		switch choice {
		case 1:
			createStudent()
		case 2:
			getStudent()
		case 3:
			updateStudent()
		case 4:
			deleteStudent()
		case 5:
			fmt.Println("Exiting...")
			return
		default:
			fmt.Println("Invalid choice. Please select a valid option.")
		}
	}
}

func createStudent() {
	reader := bufio.NewReader(os.Stdin)
	var rawName string
	var age int
	var rawGrade string

	fmt.Print("Enter student name: ")
	rawName, _ = reader.ReadString('\n')
	name := strings.ReplaceAll(rawName, "\n", "")
	fmt.Print("Enter student age: ")
	fmt.Fscanf(reader, "%d\n", &age)
	fmt.Print("Enter student grade: ")
	rawGrade, _ = reader.ReadString('\n')
	grade := strings.ReplaceAll(rawGrade, "\n", "")

	newStudent := Student{Name: name, Age: age, Grade: grade}
	postBody, _ := json.Marshal(newStudent)
	response, err := http.Post("http://localhost:3000/students", "application/json", bytes.NewBuffer(postBody))
	if err != nil {
		fmt.Println("POST request error:", err)
		return
	}
	defer response.Body.Close()

	fmt.Println("\nPOST Response Status:", response.Status)

	decoder := json.NewDecoder(response.Body)
	var createdStudent Student
	err = decoder.Decode(&createdStudent)
	if err != nil {
		fmt.Println("Error decoding response:", err)
		fmt.Println()
		return
	}

	fmt.Println("Student ID:", createdStudent.ID)
	fmt.Println()
}

func getStudent() {
	var studentID int

	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter student ID: ")
	_, err := fmt.Fscanf(reader, "%d\n", &studentID)
	if err != nil {
		fmt.Println("Invalid input. Please enter a valid ID.\n")
		return
	}
	if studentID <= 0 {
		fmt.Println("Invalid ID. ID must be greater than 0.\n")
		return
	}

	response, err := http.Get(fmt.Sprintf("http://localhost:3000/students/%d", studentID))
	if err != nil {
		fmt.Println("GET request error:", err)
		fmt.Println("Would you like to try again? (Y/N)")
		var retry string
		fmt.Fscanf(reader, "%s\n", &retry)
		if retry == "Y" || retry == "y" {
			getStudent()
		}
		return
	}
	defer response.Body.Close()

	fmt.Println("\nGET Response Status:", response.Status)

	if response.StatusCode == http.StatusNotFound {
		fmt.Println("Student not found.\n")
		return
	}

	decoder := json.NewDecoder(response.Body)
	var student Student
	err = decoder.Decode(&student)
	if err != nil {
		fmt.Println("Error decoding response:", err)
		fmt.Println()
		return
	}

	fmt.Printf(`{"id":%d,"name":"%s","age":%d,"grade":%s}`, student.ID, student.Name, student.Age, student.Grade)
	fmt.Println("\n")
}

// {"id":10,"name":"Emil Ulvagården\n","age":20,"grade":"C\n"}

func updateStudent() {
	reader := bufio.NewReader(os.Stdin)
	var studentID int
	var rawName string
	var age int
	var rawGrade string

	fmt.Print("Enter student ID to update: ")
	_, err := fmt.Fscanf(reader, "%d\n", &studentID)
	if err != nil {
		fmt.Println("Invalid input. Please enter a valid ID.\n")
		return
	}
	if studentID <= 0 {
		fmt.Println("Invalid ID. ID must be greater than 0.\n")
		return
	}

	fmt.Print("Enter student name: ")
	rawName, _ = reader.ReadString('\n')
	name := strings.ReplaceAll(rawName, "\n", "")
	fmt.Print("Enter student age: ")
	fmt.Fscanf(reader, "%d\n", &age)
	fmt.Print("Enter student grade: ")
	rawGrade, _ = reader.ReadString('\n')
	grade := strings.ReplaceAll(rawGrade, "\n", "")

	newStudent := Student{Name: name, Age: age, Grade: grade}

	putBody, _ := json.Marshal(newStudent)
	request, _ := http.NewRequest(http.MethodPut, fmt.Sprintf("http://localhost:3000/students/%d", studentID), bytes.NewBuffer(putBody))
	request.Header.Set("Content-Type", "application/json")
	response, err := http.DefaultClient.Do(request)
	if err != nil {
		fmt.Println("PUT request error:", err)
		fmt.Println("Would you like to try again? (Y/N)")
		var retry string
		fmt.Fscanf(reader, "%s\n", &retry)
		if retry == "Y" || retry == "y" {
			updateStudent()
		}
		return
	}
	defer response.Body.Close()

	fmt.Println("\nPUT Response Status:", response.Status)
	fmt.Println()
}

func deleteStudent() {
	var studentID int
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter student ID to delete: ")
	_, err := fmt.Fscanf(reader, "%d\n", &studentID)
	if err != nil {
		fmt.Println("Invalid input. Please enter a valid ID.\n")
		return
	}
	if studentID <= 0 {
		fmt.Println("Invalid ID. ID must be greater than 0.\n")
		return
	}

	request, _ := http.NewRequest(http.MethodDelete, fmt.Sprintf("http://localhost:3000/students/%d", studentID), nil)
	response, err := http.DefaultClient.Do(request)
	if err != nil {
		fmt.Println("DELETE request error:", err)
		fmt.Println("Would you like to try again? (Y/N)")
		var retry string
		fmt.Fscanf(reader, "%s\n", &retry)
		if retry == "Y" || retry == "y" {
			deleteStudent()
		}
		return
	}
	defer response.Body.Close()

	fmt.Println("\nDELETE Response Status:", response.Status)
	fmt.Println()
}
