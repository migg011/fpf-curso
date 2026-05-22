package main

import "fmt"

func matriz(vetor []int) {
	for i := 0; i < len(vetor); i++ {
		fmt.Println(vetor[i])
	}
}

func matriz2D(vetor [][]int) {
	for i := 0; i < len(vetor); i++ {
		fmt.Println("camada: ", vetor[i])
		for j := 0; j < len(vetor[i]); j++ {
			fmt.Print("elementos: ", vetor[i][j], "\n")
		}
		fmt.Println()
	}

}

func matriz3D(vetor [][][]int) {
	for i := 0; i < len(vetor); i++ {
		fmt.Println("camada1: ", vetor[i])
		for j := 0; j < len(vetor[i]); j++ {
			fmt.Print("camada2 ", vetor[i][j], "\n")
			for k := 0; k < len(vetor[i][j]); k++ {
				fmt.Print("camada3 ", vetor[i][j][k], "\n")
			}
			fmt.Println()
		}
		fmt.Println()
	}
}

func main() {

	vetor := []int{6, 1, 6, 8, 4}
	matriz(vetor)

	vetor2D := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	matriz2D(vetor2D)

	vetor3D := [][][]int{
		{
			{1, 2, 4},
			{3, 4, 5},
		},
		{
			{6, 7, 8},
			{9, 10, 11},
			{12, 13, 14},
		},
	}
	matriz3D(vetor3D)
}
