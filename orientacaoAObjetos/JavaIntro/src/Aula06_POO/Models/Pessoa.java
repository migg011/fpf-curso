package Aula06_POO.Models;

public class Pessoa {
    public String nome;
    protected int idade;
    String cidade;
    private double salario;

    public Pessoa(String nome, int idade, String cidade,  double salario) {
        this.nome = nome;
        this.idade = idade;
        this.cidade = cidade;
        this.salario = salario;
    }

    public void exibirInfoPublica(){
        System.out.printf("Nome: %s - Idade: %d - Cidade: %s",this.nome, this.idade, this.cidade );
    }

    protected void exibirProtegido(){
        System.out.printf("Metodo Protegido: idade - %s%n", idade);
    }

    private void exibirPrivado(){
        System.out.println("Metodo Privado: acessivel so dentro da classe Pessoa");
    }

    public void testarPrivadoDentro(){
        exibirPrivado();
    }

    public double getSalario(){
        return this.salario;
    }

    public void setSalario(double salario){
        this.salario = salario;
    }
}
