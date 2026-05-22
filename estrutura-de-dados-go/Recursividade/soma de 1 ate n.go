package main

import "fmt"

func De1Ate(n int) int {
	if n == 0 {
		return 0
	} else {
		return n + De1Ate(n-1)
	}
}
func main() {
	fmt.Println(De1Ate(5))
}
