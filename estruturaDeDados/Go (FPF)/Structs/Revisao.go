package main

import (
	"fmt"
	"math/rand"
)

type Carro struct {
	Marca   string
	Ano     int
	KM      int
	Renavan int
}

var carros = make(map[int]Carro)
var ID = 0

func read() {
	var buscaCarro int
	fmt.Printf("digite o ID do carro (0 a quantidade criada\nanteriormente) que deseja buscar: ")
	fmt.Scan(&buscaCarro)

	carro, sim := carros[buscaCarro]
	if sim {
		fmt.Println(carro)
	}
}

//func update() {
//	var buscaRenavan int
//
//	fmt.Println("digite o renavan do veiculo: ")
//	fmt.Scan(&buscaRenavan)
//
//	renavan, sim := carros[buscaRenavan]
//	if sim {
//
//	}
//}

func menuCriar() {

	var opcao int
	var quantidade int

	fmt.Println("Quantos carros deseja criar: ")
	fmt.Scan(&quantidade)

	for i := 0; i < quantidade; i++ {
		fmt.Println("CARROS DISPONIVEIS")
		fmt.Println("1 - Ford")
		fmt.Println("2 - Toyota")
		fmt.Println("3 - Honda")
		fmt.Println("escolha sua preferencia: ")
		fmt.Scan(&opcao)
		switch opcao {
		case 1:
			criarCarro(1)
		case 2:
			criarCarro(2)
		case 3:
			criarCarro(3)
		default:
			fmt.Println("opcao invalida")
		}
	}
}

func criarCarro(n int) {
	switch n {
	case 1:
		carros[ID] = Carro{Marca: "Ford", Ano: 2026, KM: rand.Intn(100000), Renavan: rand.Intn(10)}
		ID++
	case 2:
		carros[ID] = Carro{Marca: "Toyota", Ano: 2026, KM: rand.Intn(100000), Renavan: rand.Intn(10)}
		ID++
	case 3:
		carros[ID] = Carro{Marca: "Honda", Ano: 2026, KM: rand.Intn(100000), Renavan: rand.Intn(10)}
		ID++
	}
}

func main() {
	menuCriar()
	read()
}
