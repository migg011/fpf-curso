package main

import "fmt"

func passagem_por_valor(numero int) {
	//cria uma variavel dentro da função
	numero = numero * numero
}

func passagem_por_ref(numero *int) {
	//modifica diretamente o valor de numero
	*numero = *numero * *numero
}

func main() {
	var numero int

	numero = 10

	fmt.Println("1 - numero: ", numero)
	passagem_por_valor(numero)
	fmt.Println("2 - numero: ", numero)
	passagem_por_ref(&numero)
	fmt.Println("3 - numero: ", numero)

}
