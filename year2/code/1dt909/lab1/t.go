package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Usage: go run t.go pX.go numTests")
		return
	}

	numTests := 10
	fileName := os.Args[1]

	for i := 0; i < numTests; i++ {
		//fmt.Printf("Running Test %d\n", i)
		cmd := exec.Command("go", "run", fileName)
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		if err := cmd.Run(); err != nil {
			fmt.Printf("Test %d failed: %s\n", i, err)
			return
		}
	}
	fmt.Println("All tests passed successfully!")
}
