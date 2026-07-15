package main

import (
	"fmt"
)

type Pessoa struct {
	nome  string
	idade int
	peso  float64
}

type Usuario struct {
	nome  string
	CPF   string
	idade int
}

func main() {
	pessoa1 := Pessoa{
		nome:  "miguel",
		idade: 30,
		peso:  60.1,
	}
	fmt.Println(pessoa1)

}
