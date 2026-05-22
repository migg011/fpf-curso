package main

import "fmt"

type Automovel struct {
	Modelo  string
	Ano     int
	Marca   string
	Cor     string
	Renavam int
}

func main() {

	carro := Automovel{
		Modelo:  "Eclypse",
		Ano:     1999,
		Marca:   "Toyota",
		Cor:     "Preto",
		Renavam: 12,
	}

	moto := Automovel{
		Modelo:  "CG",
		Ano:     2020,
		Marca:   "Honda",
		Cor:     "Vermelho",
		Renavam: 1,
	}

	nossoMap := make(map[int]Automovel)

	nossoMap[0] = carro
	nossoMap[1] = moto

	fmt.Println(nossoMap)

}
