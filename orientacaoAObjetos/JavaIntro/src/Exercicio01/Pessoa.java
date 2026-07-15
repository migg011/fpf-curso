package Exercicio01;

public class Pessoa {
    public String nome;
    public int idade;
    public String cidadeNatal;

    public Pessoa(String nome, int idade, String cidadeNatal) {
        this.nome = nome;
        this.idade = idade;
        this.cidadeNatal = cidadeNatal;
    }

    public void apresentar(){
        System.out.println("Informações: ");
        System.out.println("- Nome: "+ this.nome);
        System.out.println("- Idade: "+ this.idade);
        System.out.println("- Cidade: "+ this.cidadeNatal);
    }
}
