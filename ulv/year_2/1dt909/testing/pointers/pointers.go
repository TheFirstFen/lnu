package pointers

import (
	"fmt"
)

func setToZero(ival *int) {
	*ival = 0
}

func Pointers() {
	i := 1
	fmt.Println("i = ", i)
	setToZero(&i)
	fmt.Println("i = ", i)
}