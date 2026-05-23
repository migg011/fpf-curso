package main

import "fmt"

func main() {
	var produto01 int
	var ponteiro *int

	produto01 = 10
	produto02 := produto01

	//recebe o endereço de memoria no produto01
	ponteiro = &produto01

	fmt.Println("produto01: ", produto01)
	fmt.Println("produto02: ", produto02)

	//mostra o endereço de memoria
	fmt.Println("ponteiro ", ponteiro)

	//mostra o conteudo
	fmt.Println("ponteiro ", *ponteiro)

}
