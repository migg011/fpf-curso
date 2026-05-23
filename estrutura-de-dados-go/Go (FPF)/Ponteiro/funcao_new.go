package main

import "fmt"

func main() {

	p := new(int)
	fmt.Println(p)
	fmt.Println(*p)

	var pon *int
	fmt.Println(pon)
	fmt.Println(*pon)

}
