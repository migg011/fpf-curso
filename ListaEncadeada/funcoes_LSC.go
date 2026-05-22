package main

import "fmt"

type No1 struct {
	valor int
	prox  *No1
}

func printLista(lista *No1) {
	atual := lista
	for atual != nil {
		fmt.Println(atual.valor)
		atual = atual.prox
	}
}

func append(lista *No1, valor int) {
	atual := lista
	for atual.prox != nil {
		atual = atual.prox
	}
	atual.prox = &No1{valor: valor, prox: nil}
}

func variosAppend(lista *No1, valor int) {
	atual := lista
	for i := 0; i < valor; i++ {
		atual.prox = &No1{valor: i, prox: nil}
		atual = atual.prox
	}
}

func main() {
	head := &No1{valor: -1, prox: nil}
	printLista(head)
	append(head, 10)
	printLista(head)
	variosAppend(head, 5)
	printLista(head)
}
