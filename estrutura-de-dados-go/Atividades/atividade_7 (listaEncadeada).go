package main

import "fmt"

//O usuário deve poder inserir quantos nós desejar, remover um nó por index ou por valor.
//
//Cada nó da lista terá Index, Valor e o endereço para o próximo.
//
//Será possível remover qualquer elemento, com exceção do primeiro.
//Quando declarar o ponteiro para o head use head = new(Node) ou node := &Node{}.

var lista = make([]int, 0)

func inicarLista() {

	var opcao int

	for {
		fmt.Println("LISTA DUPLAMENTE CADEADA")
		fmt.Println("1 - Inserir na nó na lista ")
		fmt.Println("2 - Remover um nó ")
		fmt.Println("3 - Imprimir lista ")
		fmt.Scanln(&opcao)

		switch opcao {
		case 1:

		}
	}
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

func removerNo(lista []int, valor int) {
	lista
}
