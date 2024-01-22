package main

import "fmt"

func setToZero(iptr *int) {
	*iptr = 0
}

func main() {
	i := 1
	a := &i
	b := i
	fmt.Println("i=", i, "&i=", &i)
	setToZero(&i)
	fmt.Println("i=", i, "&i=", &i)
	fmt.Println("a=", a, "*a=", *a, "&a=", &a)
	fmt.Println("b=", b, "&b=", &b)
}
