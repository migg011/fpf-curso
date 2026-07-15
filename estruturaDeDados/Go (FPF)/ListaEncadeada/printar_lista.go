package main

import "fmt"

type No struct {
	valor   int
	proximo *No
}

func imprimirLista(lista *No) {
	atual := lista
	for atual != nil {
		fmt.Println(atual.valor)
		atual = atual.proximo
	}

}
