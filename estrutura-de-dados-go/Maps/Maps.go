package main

import "fmt"

func main() {

	//exemplo 1
	idades := map[string]int{"ana": 29, "carlos": 81, "alexandre": 35}
	fmt.Println(idades)

	//exemplo 2
	idades = make(map[string]int)
	idades["ana"] = 26

	idades1 := map[string]int{
		"ana":    26,
		"carlos": 81,
	}

	idades1["alexandre"] = 35
	idades1["fabio"] = 13
	idades1["jose"] = 82

	delete(idades, "jose")

	for nome, idade := range idades1 {
		fmt.Println(nome, idade)
	}
}
