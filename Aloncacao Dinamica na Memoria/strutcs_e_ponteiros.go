package main

import "fmt"

type Carro struct {
	Marca  string
	modelo string
	ano    int
}

func main() {

	var ponteiro *Carro
	var carro Carro

	carro = Carro{
		Marca:  "Fiat",
		modelo: "Uno",
		ano:    2010,
	}

	ponteiro = &carro
	
	fmt.Println(ponteiro.Marca)
	fmt.Println(ponteiro.modelo)
	fmt.Println(ponteiro.ano)

}
