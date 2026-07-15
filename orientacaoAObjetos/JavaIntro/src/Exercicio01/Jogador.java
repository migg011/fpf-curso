package Exercicio01;
import java.util.List;

public class Jogador extends Pessoa {

    public Carta[] baralho;

    public Jogador(String nome, int idade,  String cidadeNatal) {
        super(nome, idade, cidadeNatal);
        this.baralho = new Carta[3];
    }
}
