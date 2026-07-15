package main

import (
	"fmt"
	"os"
	"time"
)

func logBinaria(msg string) {
	agora := time.Now()
	timestamp := agora.Format("2006-01-02 15:04:05: ")
	//abre o .log
	file, err := os.OpenFile("busca.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println("erro ao abrir log:", err)
		return
	}
	//fecha o .log
	defer file.Close()

	if _, err := file.WriteString(timestamp + msg + "\n"); err != nil {
		fmt.Println("erro ao escrever log:", err)
	}
}

func miliseg(d time.Duration) float64 {
	return float64(d.Nanoseconds()) / 1e6
}

// iterativa
func buscaBinariaIte(lista []int, encontrar int) int {
	comeco := 0
	fim := len(lista) - 1

	for comeco <= fim {
		subSlice := lista[comeco : fim+1]
		msg := fmt.Sprintf("Analisando sub-slice: %v", subSlice)

		fmt.Println(msg)
		logBinaria(msg)
		meio := (comeco + fim) / 2
		if lista[meio] == encontrar {
			return meio
		} else if lista[meio] < encontrar {
			comeco = meio + 1
		} else {
			fim = meio - 1
		}
	}
	return -1
}

// recursiva
func buscaBinariaRec(lista []int, encontrar int, inicio int, fim int) int {

	if inicio > fim {
		return -1
	}

	subSlice := lista[inicio : fim+1]
	msg := fmt.Sprintf("Analisando sub-slice: %v", subSlice)

	fmt.Println(msg)
	logBinaria(msg)

	meio := (inicio + fim) / 2

	if lista[meio] == encontrar {
		return meio
	} else if lista[meio] < encontrar {
		return buscaBinariaRec(lista, encontrar, meio+1, fim)
	} else {
		return buscaBinariaRec(lista, encontrar, inicio, meio-1)
	}

}

func main() {

	var tamanhoLista, procurar int

	fmt.Print("digite o *tamanho* da lista que deseja criar: ")
	fmt.Scan(&tamanhoLista)

	if tamanhoLista <= 0 {
		fmt.Println("ERRO: crie uma lista maior que 0")
		return
	}

	lista := make([]int, tamanhoLista)
	for i := 0; i < tamanhoLista; i++ {
		lista[i] = i
	}

	fmt.Printf("foi criado uma lista de tamanho %d, com numeros ordenados de 0 a %d\n", tamanhoLista, tamanhoLista-1)
	fmt.Println("sua lista: ", lista)

	fmt.Print("digite o numero que voce deseja procurar dentro da lista: ")
	fmt.Scan(&procurar)

	logBinaria("--- INICIANDO BUSCA RECURSIVA ---")
	comeco1 := time.Now()
	fmt.Println("Busca Binaria Recursiva: ", buscaBinariaRec(lista, procurar, 0, len(lista)-1))
	duracaoRe := time.Since(comeco1)
	logBinaria(fmt.Sprintf("Resultado: Alvo %d | Tempo: %.2fms", procurar, miliseg(duracaoRe)))

	fmt.Println("\n")

	logBinaria("--- INICIANDO BUSCA ITERATIVA ---")
	comeco2 := time.Now()
	fmt.Println("Busca Binaria Iterativa: ", buscaBinariaIte(lista, procurar))
	duracaoIt := time.Since(comeco2)
	logBinaria(fmt.Sprintf("Resultado: Alvo %d | Tempo: %.2fms", procurar, miliseg(duracaoIt)))

	logBinaria("--- COMPARAÇÃO BUSCA BINÁRIA ---")
	logBinaria(fmt.Sprintf("N: %d | Alvo: %d | Iterativa: %.2fms | Recursiva: %.2fms | Diferença: %.2fms", tamanhoLista, procurar, miliseg(duracaoIt), miliseg(duracaoRe), miliseg(duracaoRe-duracaoIt)))

}
