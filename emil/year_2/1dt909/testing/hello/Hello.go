package main

import (
	"fmt"
	"time"

	"eu222dq.testing/greetings"
	"eu222dq.testing/pointers"
	"eu222dq.testing/person"
	
)

func sayhi(name string, c chan bool) {
	fmt.Println("Hello", name)
	c <- true
}
func main() {
	c:= make(chan bool)
	//fmt.Println("Hello, World!")
	go sayhi("world", c)
	go sayhi("golang", c)
	go sayhi("hello", c)
	go sayhi("Hello", c)
	for i:= 0; i<4; i++ {<- c}

	name := "s"

	msgs, err := greetings.Hello(name)

	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(msgs)
	}

	//i := 1
	//fmt.Println("i = ", i)
	//setToZero(i)
	//fmt.Println("i = ", i)

	pointers.Pointers()

	person.Person()

	time.Sleep(time.Second*5)
}