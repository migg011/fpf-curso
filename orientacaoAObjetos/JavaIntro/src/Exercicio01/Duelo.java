package Exercicio01;

public class Duelo {
    public Jogador jogador1;
    public Jogador jogador2;

    public Duelo(Jogador jogador1, Jogador jogador2) {
        this.jogador1 = jogador1;
        this.jogador2 = jogador2;
    }

    public void iniciarDuelo() {
        int jogadorUmCarta = 0;
        int jogadorDoisCarta = 0;

        System.out.println("O DUELO COMEÇOU");

        do {
            Carta carta1 = jogador1.baralho[jogadorUmCarta];
            Carta carta2 = jogador2.baralho[jogadorDoisCarta];

            int danoJogadorUm = (carta1.ataque * ((int) (Math.random() * 4) + 1)) - carta2.defesa;

            if (danoJogadorUm < 0) {
                danoJogadorUm = 0;
            }
            carta2.ponto_de_vida -= danoJogadorUm;

            int danoJogadorDois = (carta2.ataque * ((int) (Math.random() * 4) + 1)) - carta1.defesa;

            if (danoJogadorDois < 0) {
                danoJogadorDois = 0;
            }
            carta1.ponto_de_vida -= danoJogadorDois;

            if (carta1.ponto_de_vida <= 0) {
                System.out.println(carta1.nome + " do jogador 1 foi eliminada");
                jogadorUmCarta++;
            }
            if (carta2.ponto_de_vida <= 0) {
                System.out.println(carta2.nome + " do jogador 2 foi eliminada");
                jogadorDoisCarta++;
            }

        } while (jogadorUmCarta < 3 && jogadorDoisCarta < 3);

        System.out.println("FIM DE JOGO");
        if (jogadorUmCarta == 3) {
            System.out.println("Jogador 2 venceu o duelo");
        } else {
            System.out.println("Jogador 1 venceu o duelo");
        }
    }
}