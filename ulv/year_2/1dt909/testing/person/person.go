package person 

import (
	"fmt"
)

type person struct {
	name string
	age int
}

func Person() {
	p1 := person{"John", 20}
	fmt.Println(p1)
}