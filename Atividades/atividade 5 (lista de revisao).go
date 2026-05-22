package main

import (
	"fmt"
	"math/rand"
)

// questao 1
func Fila() {

	lista := []int{}

	fmt.Println("1) nova lista: ", lista)

	for i := 0; i <= 4; i++ {
		lista = append(lista, rand.Intn(5))
	}

	fmt.Println("2) elementos inseridos", lista)

	tamanhoLista := len(lista)

	for i := 0; i < tamanhoLista; i++ {
		fmt.Printf("3) %d remoção : %d\n", i, lista)
		lista = lista[1:]
	}
	fmt.Println("4) tamanho lista: ", lista)
}

func Pilha() {

	lista := []int{}

	fmt.Println("nova lista: ", lista)

	for i := 0; i <= 4; i++ {
		lista = append(lista, rand.Intn(5))
	}

	fmt.Println("elementos inseridos", lista)

	tamanhoLista := len(lista)

	for i := 0; i < tamanhoLista; i++ {
		fmt.Printf("3) %d remoção : %d\n", i+1, lista)
		lista = lista[0 : len(lista)-1]
	}

	fmt.Println("4) tamanho lista: ", lista)

}

// questao 2
func somaAteN(n int) int {
	if n == 0 {
		return 0
	} else {
		return n + somaAteN(n-1)
	}
}

//3 - A função deve receber um número inteiro positivo e retornar quantos dígitos esse número possui.
//Exemplo:
//Entrada: 53827
//Saída: 5

func QuantosDigitos(n int) int {
	contador := 0
	if n == 0 {
		return 1
	} else {
		for n > 0 {
			n = n / 10
			contador++
		}
	}
	return contador
}

//questao 4
//4 - Descreva o funcionamento dos seguintes algoritmos de ordenação:

//● Bubble Sort: flutua o maior numero para o ultimo index da lista (direita pra esquerda)
//● Insertion Sort: percorre a lista verificando o menor numero e quando é "achado" é colocado
// no seu devido index (esquerda pra direita)
//● Selection Sort: faz a comparação dos index vizinhos verificando o menor numero, assim fazendo a troca dos vizinhos (esquerda pra direita)
//● Merge Sort: divide a lista em pequenos grupos, ordena separadamente e no final junta os grupos numa lista ordenada]

// questao 5
func matrizIdentidade() [][]int {

	matriz := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}

	for i := 0; i < len(matriz); i++ {
		for j := 0; j < len(matriz[i]); j++ {
			if i == j {
				matriz[i][j] = 1
			} else {
				matriz[i][j] = 0
			}
		}
	}
	for i := 0; i < len(matriz); i++ {
		fmt.Println(matriz[i])
	}

	return matriz

}

//questao6

func multiplicacaoMatriz(matriz [][]int) int {

	multi := 1

	for i := 0; i < len(matriz); i++ {
		for j := 0; j < len(matriz[i]); j++ {
			if matriz[i][j] > 0 {
				multi *= matriz[i][j]
			}
		}
	}

	return multi
}

func main() {

}
