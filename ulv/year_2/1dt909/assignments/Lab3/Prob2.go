package main

import (
    "fmt"
    "net/http"
    "bytes"
    "encoding/json"
    "os"
    "strings"
    "bufio"
	"strconv"
)

const (
    baseURL = "http://localhost:3000/students"
)

type Student struct {
    Studentid int    `json:"studentid"`
    Name      string `json:"name"`
    Age       int    `json:"age"`
    Grade     string `json:"grade"`
}

func main() {
    reader := bufio.NewReader(os.Stdin)

    for {
        fmt.Println("Select Operation:")
        fmt.Println("1. Create Student")
        fmt.Println("2. Get Student")
        fmt.Println("3. Update Student")
        fmt.Println("4. Delete Student")
        fmt.Println("5. Exit")

        fmt.Print("Enter your choice: ")
        choiceStr, _ := reader.ReadString('\n')
        choiceStr = strings.TrimSpace(choiceStr)
        choice, err := strconv.Atoi(choiceStr)
        if err != nil {
            fmt.Println("Invalid input. Please enter a number.")
            continue
        }

        switch choice {
        case 1:
            addStudent()
        case 2:
            getStudent()
        case 3:
            updateStudent()
        case 4:
            deleteStudent()
        case 5:
            fmt.Println("Exiting")
            os.Exit(0)
        default:
            fmt.Println("Invalid choice. Please select a valid option.")
        }
    }
}

func addStudent() {
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
    resp, err := http.Post(baseURL, "application/json", bytes.NewBuffer(postBody))

    if err != nil {
        fmt.Println(err)
        return
    }
    defer resp.Body.Close()

    fmt.Println("\nResponse Status:", resp.Status)

    decode := json.NewDecoder(resp.Body)
    var result Student
    err = decode.Decode(&result)
    if err != nil {
        fmt.Println("Error: ", err)
        return
    }

    fmt.Println("Student ID:", result.Studentid)
}

func getStudent() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter student ID: ")
    idStr, _ := reader.ReadString('\n')
    studentID, err := strconv.Atoi(strings.TrimSpace(idStr))
    if err != nil {
        fmt.Println("Invalid input. Please enter a valid number.")
        return
    }

    resp, err := http.Get(fmt.Sprintf("%s/%d", baseURL, studentID))
    if err != nil {
        fmt.Println("Request error: ", err)
        return
    }
    defer resp.Body.Close()

    fmt.Println("\nResponse Status:", resp.Status)
    if resp.StatusCode == http.StatusNotFound {
        fmt.Println("Student not found.")
        return
    }
    decode := json.NewDecoder(resp.Body)
    var result Student
    err = decode.Decode(&result)
    if err != nil {
        fmt.Println("Error: ", err)
        return
    }

    fmt.Println("Student ID:", result.Studentid)
    fmt.Println("Name:", result.Name)
    fmt.Println("Age:", result.Age)
    fmt.Println("Grade:", result.Grade)
}

func updateStudent() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter student ID that is to be updated: ")
    idStr, _ := reader.ReadString('\n')
    studentID, err := strconv.Atoi(strings.TrimSpace(idStr))
    if err != nil {
        fmt.Println("Invalid input. Please enter a valid number.")
        return
    }

    fmt.Print("Enter student name: ")
    rawName, _ := reader.ReadString('\n')
    name := strings.TrimSpace(rawName)

    fmt.Print("Enter student age: ")
    ageStr, _ := reader.ReadString('\n')
    age, err := strconv.Atoi(strings.TrimSpace(ageStr))
    if err != nil {
        fmt.Println("Invalid age input. Please enter a valid number.")
        return
    }

    fmt.Print("Enter student grade: ")
    rawGrade, _ := reader.ReadString('\n')
    grade := strings.TrimSpace(rawGrade)

    updatedStudent := Student{Studentid: studentID, Name: name, Age: age, Grade: grade}

    putBody, _ := json.Marshal(updatedStudent)
    request, _ := http.NewRequest("PUT", fmt.Sprintf("%s/%d", baseURL, studentID), bytes.NewBuffer(putBody))

    request.Header.Set("Content-Type", "application/json")
    resp, err := http.DefaultClient.Do(request)
    if err != nil {
        fmt.Println("Request error: ", err)
        return
    }
    defer resp.Body.Close()

    fmt.Println("\nResponse Status:", resp.Status)
}

func deleteStudent() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter student ID that is to be deleted: ")
    idStr, _ := reader.ReadString('\n')
    studentID, err := strconv.Atoi(strings.TrimSpace(idStr))
    if err != nil {
        fmt.Println("Invalid input. Please enter a valid number.")
        return
    }

    request, _ := http.NewRequest("DELETE", fmt.Sprintf("%s/%d", baseURL, studentID), nil)
    resp, err := http.DefaultClient.Do(request)
    if err != nil {
        fmt.Println("Request error: ", err)
        return
    }
    defer resp.Body.Close()

    fmt.Println("\nResponse Status:", resp.Status)
}
