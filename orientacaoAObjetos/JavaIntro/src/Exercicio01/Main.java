package Exercicio01;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        List<Carta> BancoDeCartas = new ArrayList<>();

        BancoDeCartas.add(new Carta("Dragão Flamejante", 7, 4, 20));
        BancoDeCartas.add(new Carta("Fênix de Cinzas", 6, 3, 18));
        BancoDeCartas.add(new Carta("Golem de Pedra", 4, 9, 25));
        BancoDeCartas.add(new Carta("Mago Arcano", 5, 4, 16));
        BancoDeCartas.add(new Carta("Serpente Abissal", 9, 3, 18));
        BancoDeCartas.add(new Carta("Anjo da Luz", 6, 5, 18));
        BancoDeCartas.add(new Carta("Hidra de Escamas", 8, 6, 25));
        BancoDeCartas.add(new Carta("Guardião Celestial", 5, 8, 22));
        BancoDeCartas.add(new Carta("Elemental de Fogo", 9, 3, 16));
        BancoDeCartas.add(new Carta("Centauro Guerreiro:", 8, 5, 20));

        BancoDeCartas.add(new Carta("Elfo da Floresta:", 3, 2, 12));
        BancoDeCartas.add(new Carta("Cavaleiro de Ébano:", 5, 6, 15));
        BancoDeCartas.add(new Carta("Assassino das Sombras:", 8, 2, 14));
        BancoDeCartas.add(new Carta("Troll da Ponte:", 6, 7, 22));
        BancoDeCartas.add(new Carta("Lobisomem da Noite:", 7, 5, 20));
        BancoDeCartas.add(new Carta("Necromante Sombrio:", 7, 3, 15));
        BancoDeCartas.add(new Carta("Goblin Selvagem:", 3, 2, 10));
        BancoDeCartas.add(new Carta("Vampiro Noturno:", 7, 4, 17));
        BancoDeCartas.add(new Carta("Corruptor de Almas:", 6, 4, 14));
        BancoDeCartas.add(new Carta("Monstro das Profundezas::", 10, 2, 18));

        Jogador jogador1 = new Jogador("Yugi", 16, "Manaus");
        Jogador jogador2 = new Jogador("Kaiba", 17, "Parintins ");

        for (int i = 0; i < 3; i++) {
            int indiceAleatorio1 = (int) (Math.random() * BancoDeCartas.size());
            jogador1.baralho[i] = BancoDeCartas.remove(indiceAleatorio1);

            int indiceAleatorio2 = (int) (Math.random() * BancoDeCartas.size());
            jogador2.baralho[i] = BancoDeCartas.remove(indiceAleatorio2);
        }

        jogador1.apresentar();
        jogador2.apresentar();

        Duelo partida = new Duelo(jogador1, jogador2);
        partida.iniciarDuelo();

    }
}
d