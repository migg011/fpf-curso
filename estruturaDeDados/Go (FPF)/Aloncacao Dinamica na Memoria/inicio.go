package main

import "fmt"

func main() {
	var a int
	var b int
	var p *int

	fmt.Println("digite um numero inteiro: ")
	fmt.Scanln(&a)

	b = a
	p = &a

	fmt.Println("variavel a: ", a)
	fmt.Println("variavel b: ", b)
	fmt.Println("ponteiro p: ", p)
	fmt.Println("ponteiro p (conteudo): ", *p)

	fmt.Println("digite outro valor inteiro para a: ")
	fmt.Scanln(&*p)

	fmt.Println("variavel a: ", a)
	fmt.Println("variavel b: ", b)
	fmt.Println("ponteiro p: ", p)
	fmt.Println("ponteiro p (conteudo): ", *p)
}
