package main

import "fmt"

type No struct {
	valor int
	prox  *No
}

type Lista struct {
	inicio *No
}

func adicionarNo(l *Lista, valor int) {
	novoNo := &No{valor: valor}

	if l.inicio == nil {
		l.inicio = novoNo
		return
	}

	atual := l.inicio
	for atual.prox != nil {
		atual = atual.prox
	}

	atual.prox = novoNo
}

func mostrarLista(l *Lista) {
	atual := l.inicio

	for atual != nil {
		fmt.Print(atual.valor)
		if atual.prox != nil {
			fmt.Print(" proximo: ")
		}
		atual = atual.prox
	}
	fmt.Println()
}

func main() {
	var lista Lista

	adicionarNo(&lista, 10)
	mostrarLista(&lista)
	adicionarNo(&lista, 20)
	mostrarLista(&lista)
	adicionarNo(&lista, 30)
	mostrarLista(&lista)
}
