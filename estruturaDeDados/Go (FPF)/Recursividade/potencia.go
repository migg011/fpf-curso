package main

import "fmt"

func potencia(a, b int) int {
	if b == 0 {
		return 1
	} else if b == 1 {
		return a
	} else {
		return a * potencia(a, b-1)
	}
}
func main() {
	fmt.Println(potencia(3, 3))
}
