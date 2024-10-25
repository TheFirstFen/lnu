package main

import "fmt"

type person struct {
	name string
	age int
}

func main() {
	p1 := person{"Alcie", 10}
	fmt.Println(p1)
	p2 := person{name: "Bob"}
	p2.age = 20
	fmt.Println(p2)
}
