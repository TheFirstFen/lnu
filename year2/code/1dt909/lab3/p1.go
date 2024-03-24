package main

import (
	"bytes"
	"fmt"
	"io"
	"net/http"
)

const (
	baseURL = "http://localhost:3000/kvs"
)

func get(key string) (string, error) {
	resp, err := http.Get(fmt.Sprintf("%s/%s", baseURL, key))
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusOK {
		body, err := io.ReadAll(resp.Body)
		if err != nil {
			return "", err
		}
		return string(body), nil
	}
	return "", fmt.Errorf("failed to get value for key %s, status code: %d", key, resp.StatusCode)
}

func post(key, value string) error {
	resp, err := http.Post(fmt.Sprintf("%s/%s", baseURL, key), "text/plain", bytes.NewBufferString(value))
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusCreated {
		return nil
	}
	return fmt.Errorf("failed to put value for key %s, status code: %d", key, resp.StatusCode)
}

func delete(key string) error {
	req, err := http.NewRequest(http.MethodDelete, fmt.Sprintf("%s/%s", baseURL, key), nil)
	if err != nil {
		return err
	}

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusOK {
		return nil
	}
	return fmt.Errorf("failed to delete key %s, status code: %d", key, resp.StatusCode)
}

func main() {
	keys := []string{"first", "second", "third", "fourth"}
	values := []string{"initial", "another", "more", "done"}
	for i, key := range keys {
		if err := post(key, values[i]); err != nil {
			fmt.Printf("put %s failed: %s\n", key, err)
		}
	}

	value, err := get("first")
	if err != nil {
		fmt.Println("get first failed:", err)
	} else {
		fmt.Println("Value for key 'first':", value)
	}

	value, err = get("fifth")
	if err != nil {
		fmt.Println("get fifth failed:", err)
	} else {
		fmt.Println("Value for key 'fifth':", value)
	}

	if err := delete("third"); err != nil {
		fmt.Println("delete third failed:", err)
	}

	value, err = get("third")
	if err != nil {
		fmt.Println("get third failed:", err)
	} else {
		fmt.Println("Value for key 'third' after deletion:", value)
	}
}
