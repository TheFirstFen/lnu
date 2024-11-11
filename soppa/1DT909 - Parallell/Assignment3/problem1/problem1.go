package main

import (
	"bytes"
	"fmt"
	"io"
	"net/http"
)

const baseURL = "http://localhost:8888/kvs"

func put(key, val string) bool {

	resp, err := http.NewRequest(http.MethodPut, fmt.Sprintf("%s/%s", baseURL, key), bytes.NewBufferString(val))
	if err != nil {
		fmt.Println("Error creating PUT request:", err)
		return false
	}

	body, err := http.DefaultClient.Do(resp)
	if err != nil {
		fmt.Println("Error sending PUT request:", err)
		return false
	}
	defer body.Body.Close()

	// 201 indicates succesful creation
	return body.StatusCode == 201
}

func get(key string) (string, bool) {
	resp, err := http.Get(fmt.Sprintf("%s/%s", baseURL, key))
	if err != nil {
		return "Failed GET request", false
	}
	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "Error reading response", false
	}
	// 200 indicates succesful GET
	return string(body), resp.StatusCode == 200
}

func del(key string) bool {
	resp, err := http.NewRequest(http.MethodDelete, fmt.Sprintf("%s/%s", baseURL, key), nil)
	if err != nil {
		fmt.Println("Error creating DELETE request:", err)
		return false
	}
	body, err := http.DefaultClient.Do(resp)
	if err != nil {
		fmt.Println("Error sending DELETE request:", err)
		return false
	}
	defer body.Body.Close()
	// 200 indicates succesful deletion
	return body.StatusCode == 200

}

func main() {
	if !put("first", "initial") {
		fmt.Println("Put first failed")
	} else {
		fmt.Println("Put first succesful")
	}

	value, err := get("first")
	if !err {
		fmt.Println("Error:", value)
	} else {
		fmt.Println("Get succesful for key first, value is", value)
	}

	if !put("second", "another") {
		fmt.Println("Put second failed")
	} else {
		fmt.Println("Put second succesful")
	}
	if !put("third", "more") {
		fmt.Println("Put third failed")
	} else {
		fmt.Println("Put third succesful")
	}
	if !put("fourth", "done") {
		fmt.Println("Put fourth failed")
	} else {
		fmt.Println("Put fourth succesful")
	}

	fmt.Println("Should fail:")
	value, err = get("fifth")
	if !err {
		fmt.Print("Error:", value)
	} else {
		fmt.Print("Get succesful for key fifth, value is", value)
	}

	if !del("third") {
		fmt.Println("Delete third failed")
	} else {
		fmt.Println("Delete third succesful")
	}

	fmt.Println("Should fail:")
	value, err = get("third")
	if !err {
		fmt.Println("Error:", value)
	} else {
		fmt.Println("Get succesful for key third, value is", value)
	}
}
