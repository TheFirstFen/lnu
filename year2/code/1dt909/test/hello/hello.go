package main

import (
	"fmt"
	"log"

	"example.com/greetings"
)

func main() {
	log.SetPrefix("greetings: ")
	log.SetFlags(0)

	names := []string{"Samuel", "Samantha", "Darrin"}

	name := "Samuel"

	msg, err := greetings.Hello(name)

	msgs, errs := greetings.Hellos(names)

	if err != nil && errs != nil {
		log.Fatal(err)
	}

	fmt.Println(msg)

	for _, msg := range msgs {
		fmt.Println(msg)
	}
}