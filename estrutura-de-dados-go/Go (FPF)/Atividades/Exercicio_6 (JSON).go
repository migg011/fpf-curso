package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type Pessoa struct {
	Nome           string
	CPF            string
	DataNascimento string
	Idade          int
}

func main() {
	for {
		var opcao int
		fmt.Println("\nCRUD - PESSOAS")
		fmt.Println("1 - Cadastrar pessoa")
		fmt.Println("2 - Listar pessoas")
		fmt.Println("3 - Buscar pessoa por CPF")
		fmt.Println("4 - Atualizar pessoa")
		fmt.Println("5 - Remover pessoa")
		fmt.Println("0 - Sair")
		fmt.Print("Escolha: ")
		fmt.Scanln(&opcao)

		switch opcao {
		case 1:
			adicionarPessoa()
		case 2:
			listarPessoas()
		case 3:
			buscarPessoa()
		case 4:
			atualizarPessoa()
		case 5:
			removerPessoa()
		case 0:
			fmt.Println("finalizando...")
			return
		default:
			fmt.Println("ERRO! opcao invalida")
		}
	}
}

func adicionarPessoa() {
	arquivo := "pessoas.json"
	dados, _ := os.ReadFile(arquivo)

	var pessoas []Pessoa
	json.Unmarshal(dados, &pessoas)

	var pessoa Pessoa

	fmt.Print("nome: ")
	fmt.Scanln(&pessoa.Nome)

	fmt.Print("cpf: ")
	fmt.Scanln(&pessoa.CPF)

	for i := range pessoas {
		if pessoas[i].CPF == pessoa.CPF {
			fmt.Println("esse cpf já esta cadastrado.")
			return
		}
	}

	fmt.Print("data de nascimento: ")
	fmt.Scanln(&pessoa.DataNascimento)

	fmt.Print("idade: ")
	fmt.Scanln(&pessoa.Idade)

	pessoas = append(pessoas, pessoa)

	jsonBytes, _ := json.MarshalIndent(pessoas, "", " ")
	os.WriteFile(arquivo, jsonBytes, 0644)

	fmt.Println("pessoa adicionada.")
}

func listarPessoas() {
	arquivo := "pessoas.json"
	dados, _ := os.ReadFile(arquivo)

	var pessoas []Pessoa
	json.Unmarshal(dados, &pessoas)

	if len(pessoas) == 0 {
		fmt.Println("nenhuma pessoa cadastrada.")
		return
	}

	for i := range pessoas {
		fmt.Println("\npessoa", i+1)
		fmt.Println("nome:", pessoas[i].Nome)
		fmt.Println("cpf:", pessoas[i].CPF)
		fmt.Println("data de nascimento:", pessoas[i].DataNascimento)
		fmt.Println("idade:", pessoas[i].Idade)
	}
}

func buscarPessoa() {
	arquivo := "pessoas.json"
	dados, _ := os.ReadFile(arquivo)

	var pessoas []Pessoa
	json.Unmarshal(dados, &pessoas)

	var cpf string
	fmt.Print("digite o cpf para buscar: ")
	fmt.Scanln(&cpf)

	for i := range pessoas {
		if pessoas[i].CPF == cpf {
			fmt.Println("\npessoa encontrada:")
			fmt.Println("nome:", pessoas[i].Nome)
			fmt.Println("cpf:", pessoas[i].CPF)
			fmt.Println("data de nascimento:", pessoas[i].DataNascimento)
			fmt.Println("idade:", pessoas[i].Idade)
			return
		}
	}

	fmt.Println("pessoa não encontrada.")
}

func atualizarPessoa() {
	arquivo := "pessoas.json"
	dados, _ := os.ReadFile(arquivo)

	var pessoas []Pessoa
	json.Unmarshal(dados, &pessoas)

	var cpf string
	fmt.Print("digite o cpf da pessoa que deseja atualizar: ")
	fmt.Scanln(&cpf)

	for i := range pessoas {
		if pessoas[i].CPF == cpf {
			fmt.Print("novo nome: ")
			fmt.Scanln(&pessoas[i].Nome)

			fmt.Print("nova data de nascimento: ")
			fmt.Scanln(&pessoas[i].DataNascimento)

			fmt.Print("nova idade: ")
			fmt.Scanln(&pessoas[i].Idade)

			jsonBytes, _ := json.MarshalIndent(pessoas, "", " ")
			os.WriteFile(arquivo, jsonBytes, 0644)

			fmt.Println("pessoa atualizada.")
			return
		}
	}

	fmt.Println("pessoa não encontrada.")
}

func removerPessoa() {
	arquivo := "pessoas.json"
	dados, _ := os.ReadFile(arquivo)

	var pessoas []Pessoa
	json.Unmarshal(dados, &pessoas)

	var cpf string
	fmt.Print("digite o cpf da pessoa que deseja remover: ")
	fmt.Scanln(&cpf)

	var novaLista []Pessoa

	for i := range pessoas {
		if pessoas[i].CPF != cpf {
			novaLista = append(novaLista, pessoas[i])
		}
	}

	jsonBytes, _ := json.MarshalIndent(novaLista, "", " ")
	os.WriteFile(arquivo, jsonBytes, 0644)

	fmt.Println("pessoa excluida.")
}
