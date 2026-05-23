package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strings"
	"unicode"
)

func questao1() {
	var salario float64
	var bonus float64

	fmt.Print("digite seu salario: ")
	fmt.Scanln(&salario)
	if salario < 1000 {
		bonus = salario * 0.20
	} else {
		bonus = salario * 0.10
	}
	fmt.Println("salario final com bonus:", salario+bonus)
}

func questao2() {

	var opcao int

	fmt.Println("cardapio")
	fmt.Println("1. Pizza")
	fmt.Println("2. salada")
	fmt.Println("3. sushi")
	fmt.Print("Escolha uma opção: ")
	fmt.Scanln(&opcao)

	switch opcao {
	case 1:
		fmt.Println("voce escolheu pizza")
	case 2:
		fmt.Println("voce escolheu salada")
	case 3:
		fmt.Println("voce escolheu sushi")
	}
}

func questao3() {

	var num1 float64
	var num2 float64

	fmt.Println("digite o primeiro numero: ")
	fmt.Scanln(&num1)
	fmt.Println("digite o segundo numero: ")
	fmt.Scanln(&num2)

	var opcao int

	fmt.Println("Menu de Operações")
	fmt.Println("1. Soma")
	fmt.Println("2. Substração")
	fmt.Println("3. Multiplicação")
	fmt.Println("4. Divisão")
	fmt.Println("5. Resto Inteiro")

	fmt.Print("Escolha uma opção: ")
	fmt.Scanln(&opcao)

	var resultado float64

	switch opcao {
	case 1:
		resultado = num1 + num2
		fmt.Println("resultado da soma: ", resultado)
	case 2:
		resultado = num1 - num2
		fmt.Println("resultado da subtração: ", resultado)
	case 3:
		resultado = num1 * num2
		fmt.Println("resultado da multiplicação: ", resultado)
	case 4:
		resultado = num1 / num2
		fmt.Println("resultado da divisao: ", resultado)
	case 5:
		resultado = math.Mod(num1, num2)
		fmt.Println("resto da divisao: ", resultado)
	}
}

func questao4() {

	var peso, altura, resultado, idade float64
	var sexo int

	fmt.Println("Taxa Metabólica Basal (TMB)")
	fmt.Println("digite seu peso:")
	fmt.Scanln(&peso)

	fmt.Println("digite sua altura:")
	fmt.Scanln(&altura)

	fmt.Println("digite sua idade:")
	fmt.Scanln(&idade)

	fmt.Println("Sexo")
	fmt.Println("1 - Masculino")
	fmt.Println("2 - Feminino")
	fmt.Print("escolha sua opcao: ")
	fmt.Scanln(&sexo)

	switch sexo {
	case 1:
		resultado = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
	case 2:
		resultado = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
	}
	fmt.Printf("sua TMB é: %.2f\n", resultado)
}

func questao6() {

	var numero int
	fmt.Println("Primo?")
	fmt.Print("digite um numero: ")
	fmt.Scanln(&numero)

	if numero < 2 {
		fmt.Println("nao é primo")
		return
	}

	for i := 2; i*i <= numero; i++ {
		if numero%i == 0 {
			fmt.Println("nao é primo")
			return
		}
	}

	fmt.Println("é primo")

}

func questao7() {

	var numero, quantidade, somaPar, somaImpar int

	fmt.Print("deseja adicionar quantos numeros? ")
	fmt.Scanln(&quantidade)

	for i := 0; i < quantidade; i++ {
		fmt.Printf("digite o %d numero: ", i+1)
		fmt.Scanln(&numero)

		if numero%2 == 0 {
			somaPar += numero
		} else {
			somaImpar += numero
		}
	}

	fmt.Println("soma de todos os pares: ", somaPar)
	fmt.Println("soma de todos os impares: ", somaImpar)

}

func questao8() {

	var numero int
	fatorial := 1

	fmt.Print("digite um numero positivo: ")
	fmt.Scanln(&numero)

	for i := 2; i <= numero; i++ {
		fatorial *= i
	}

	fmt.Println("fatorial desse numero é: ", fatorial)

}

func questao9() {
	const n = 20
	a, b := 0, 1

	for i := 0; i < n; i++ {
		fmt.Print(a)
		if i < n-1 {
			fmt.Print(" ")
		}
		a, b = b, a+b
	}
	fmt.Println()
}

// muito dificil  :/

func questao10() {

	var n int
	fmt.Print("Digite um numero inteiro: ")
	fmt.Scanln(&n)

	if n == 0 {
		fmt.Println(0)
		return
	}

	neg := false
	if n < 0 {
		neg = true
		n = -n
	}

	reverso := 0
	for n > 0 {
		dig := n % 10
		reverso = reverso*10 + dig
		n /= 10
	}

	if neg {
		reverso = -reverso
	}

	fmt.Println("Numero reverso:", reverso)
}

func questao11() {

	in := bufio.NewReader(os.Stdin)

	fmt.Print("Digite uma palavra ou frase: ")
	texto, _ := in.ReadString('\n')
	texto = strings.TrimSpace(texto)
	texto = strings.ToLower(texto)

	var b strings.Builder
	for _, r := range texto {
		if unicode.IsLetter(r) || unicode.IsDigit(r) {
			b.WriteRune(r)
		}
	}

	runes := []rune(b.String())
	i, j := 0, len(runes)-1
	for i < j {
		if runes[i] != runes[j] {
			fmt.Println("Nao é palindromo.")
			return
		}
		i++
		j--
	}

	fmt.Println("É palindromo.")
}

func questao12() {

	numeros := [10]int{}
	pares := []int{}
	impares := []int{}

	fmt.Println("Digite 10 numeros a seguir")

	for i := 0; i < 10; i++ {
		fmt.Printf("Digite o %d numero: ", i+1)
		fmt.Scanln(&numeros[i])
	}

	for _, num := range numeros {
		if num%2 == 0 {
			pares = append(pares, num)
		} else {
			impares = append(impares, num)
		}
	}

	sort.Ints(pares)
	sort.Ints(impares)

	fmt.Println(numeros)
	fmt.Println(pares)
	fmt.Println(impares)

}

func questao13() {

	vetor := []string{}
	numericos := []string{}
	naoNumericos := []string{}
	var entrada string

	fmt.Println("digite -1 para encerrar")

	for {
		fmt.Print("adicione: ")
		fmt.Scanln(&entrada)

		if entrada == "-1" {
			break
		} else {
			vetor = append(vetor, entrada)
		}
	}

	for i := 0; i < len(vetor); i++ {

		s := vetor[i]

		if len(s) == 1 && s[0] >= '1' && s[0] <= '9' {
			numericos = append(numericos, s)
		} else {
			naoNumericos = append(naoNumericos, s)
		}
	}

	fmt.Println("numericos: ", numericos)
	fmt.Println("nao numerico: ", naoNumericos)

}

func questao14() {

	var palavra string

	fmt.Println("digite sua palavra: ")
	fmt.Scanln(&palavra)
	palavra = strings.ToLower(palavra)

	r := []rune(palavra)
	j := len(r) - 1

	for i := 0; i < j; {
		if r[i] != r[j] {
			fmt.Println("sua palavra NAO é um palindromo! ")
			return
		} else {
			i++
			j--
		}
	}

	fmt.Println("é palindromo! ")

}

func questao15() {
	lista := []int{1, 2, 2, 3, 1, 4, 4, 5}

	seen := make(map[int]struct{})
	unicos := []int{}

	for _, v := range lista {
		if _, ok := seen[v]; !ok {
			seen[v] = struct{}{}
			unicos = append(unicos, v)
		}
	}

	fmt.Println("lista original: ", lista)
	fmt.Println("elementos unicos: ", unicos)
}

func questao16() {
	lista1 := []int{1, 3, 5, 7}
	lista2 := []int{2, 4, 6}

	intercalada := []int{}
	i, j := 0, 0

	for i < len(lista1) || j < len(lista2) {
		if i < len(lista1) {
			intercalada = append(intercalada, lista1[i])
			i++
		}
		if j < len(lista2) {
			intercalada = append(intercalada, lista2[j])
			j++
		}
	}

	fmt.Println("lista 1:", lista1)
	fmt.Println("lista 2:", lista2)
	fmt.Println("intercalada:", intercalada)
}

func questao17() {
	s1 := "goland, "
	s2 := "python"

	concatenada := appendStrings(s1, s2)
	fmt.Println(concatenada)

}
func appendStrings(a, b string) string {
	return a + b
}

func maior_numero(lista []int) int {
	maior := lista[0]
	for _, v := range lista[1:] {
		if v > maior {
			maior = v
		}
	}
	return maior
}

func menor_numero(lista []int) int {
	menor := lista[0]
	for _, v := range lista[1:] {
		if v < menor {
			menor = v
		}
	}
	return menor
}

func questao18() {
	lista := []int{7, 2, 10, -3, 5}
	fmt.Println("lista:", lista)
	fmt.Println("maior:", maior_numero(lista))
	fmt.Println("menor:", menor_numero(lista))
}

func conta_vogais(palavra string) int {
	palavra = strings.ToLower(palavra)

	total := 0
	for _, r := range palavra {
		switch r {
		case 'a', 'e', 'i', 'o', 'u':
			total++
		}
	}
	return total
}

func questao19() {
	var palavra string
	fmt.Print("digite uma palavra: ")
	fmt.Scanln(&palavra)

	fmt.Println("total de vogais:", conta_vogais(palavra))
}

func inverte_lista(lista []int) []int {
	invertida := make([]int, len(lista))
	for i := 0; i < len(lista); i++ {
		invertida[i] = lista[len(lista)-1-i]
	}
	return invertida
}

func questao20() {
	lista := []int{1, 2, 3, 4, 5}
	fmt.Println("lista original:", lista)
	fmt.Println("lista invertida:", inverte_lista(lista))
}

func somaLista(lista []float64) float64 {
	soma := 0.0
	for _, v := range lista {
		soma += v
	}
	return soma
}

func mediaLista(lista []float64) float64 {
	return somaLista(lista) / float64(len(lista))
}

func contaParImpar(lista []float64) (pares, impares int) {
	for _, v := range lista {
		if int(v)%2 == 0 {
			pares++
		} else {
			impares++
		}
	}
	return
}

func maiorMenor(lista []float64) (maior, menor float64) {
	maior = lista[0]
	menor = lista[0]
	for _, v := range lista[1:] {
		if v > maior {
			maior = v
		}
		if v < menor {
			menor = v
		}
	}
	return
}

func maisProximoDaMedia(lista []float64, media float64) float64 {
	maisProximo := lista[0]
	menorDist := math.Abs(lista[0] - media)

	for _, v := range lista[1:] {
		dist := math.Abs(v - media)
		if dist < menorDist {
			menorDist = dist
			maisProximo = v
		}
	}
	return maisProximo
}

func estatisticas_lista(lista []float64) {
	if len(lista) == 0 {
		fmt.Println("lista vazia.")
		return
	}

	soma := somaLista(lista)
	media := mediaLista(lista)
	pares, impares := contaParImpar(lista)
	maior, menor := maiorMenor(lista)
	proximo := maisProximoDaMedia(lista, media)

	fmt.Printf("soma: %.2f\n", soma)
	fmt.Printf("media: %.2f\n", media)
	fmt.Printf("pares: %d , impares: %d\n", pares, impares)
	fmt.Printf("maior: %.2f , menor: %.2f\n", maior, menor)
	fmt.Printf("o mais proximo da media: %.2f\n", proximo)
}

func questao21() {
	lista := []float64{1, 2, 3, 4, 5, 6}
	estatisticas_lista(lista)
}

func main() {
	questao21()
}
