package main

import "fmt"

func dobra(numero *int) {
	*numero = *numero * 2
}

func main() {
	var numero int
	numero = 10
	fmt.Println("numero: ", numero)
	fmt.Println("endereço da variavel: ", &numero)
	dobra(&numero)
	fmt.Println("numero: ", numero)
	fmt.Println("endereço da variavel: ", &numero)

}
