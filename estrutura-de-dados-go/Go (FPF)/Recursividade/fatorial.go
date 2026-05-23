package main

import "fmt"

func fac(n int) int {
	if n == 1 || n == 0 {
		fmt.Println(n)
		return 1
	} else {
		return n * fac(n-1)
	}
}

func main() {
	fmt.Println(fac(5))
}
