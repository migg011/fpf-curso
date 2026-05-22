package main

import (
	"fmt"
	"os"
	"time"
)

func log(msg string) {
	agora := time.Now()
	timestamp := agora.Format("2006-01-02 15:04:05: ")
	//abre o .log
	file, err := os.OpenFile("fibonacci.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
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

// funcao para que pega o (time.Duration) e transforma o resultado em milissegundos
func ms(d time.Duration) float64 {
	return float64(d.Nanoseconds()) / 1e6
}

// funcao recursiva
func fiboRe(n int) int {
	if n == 0 {
		return 0
	} else if n == 1 {
		return 1
	} else {
		log(fmt.Sprintf("Passo {%d} : fib(%d)", n, n))
		return fiboRe(n-1) + fiboRe(n-2)
	}
}

// funcao iterativa
func fiboIt(n int) int {
	if n == 0 {
		return 0
	} else if n == 1 {
		return 1
	}
	a, b := 0, 1
	for i := 2; i <= n; i++ {
		temp := a + b
		a = b
		b = temp
		log(fmt.Sprintf("Passo {%d} : fib(%d) = %d", i, i, b))
	}
	return b
}

func main() {
	var numero int
	fmt.Print("digite um numero inteiro: ")
	fmt.Scan(&numero)

	log("--- INICIANDO FIBONACCI RECURSIVO ---")
	comeco1 := time.Now()
	retorno1 := fiboRe(numero)
	duracaoRe := time.Since(comeco1)
	fmt.Println(retorno1)
	log(fmt.Sprintf("Resultado: Fibonacci(%d) = %d | Tempo: %.2fms", numero, retorno1, ms(duracaoRe)))

	log("--- INICIANDO FIBONACCI ITERATIVO ---")
	comeco2 := time.Now()
	retorno2 := fiboIt(numero)
	duracaoIt := time.Since(comeco2)
	fmt.Println(retorno2)
	log(fmt.Sprintf("Resultado: Fibonacci(%d) = %d | Tempo: %.2fms", numero, retorno2, ms(duracaoIt)))

	log("--- COMPARAÇÃO FIBONACCI --- ")
	log(fmt.Sprintf("N: %d | Fibonacci: %d | Iterativa: %.2fms | Recursiva: %.2fms | Diferença: %.2fms", numero, retorno2, ms(duracaoIt), ms(duracaoRe), ms(duracaoRe-duracaoIt)))
}
