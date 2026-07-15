import random

class Nave:
    def __init__(self, nome, ataque_normal, ataque_especial, defesa, ponto_de_vida):
        self.nome = nome
        self.ataque_normal = ataque_normal
        self.ataque_especial = ataque_especial
        self.defesa = defesa
        self.ponto_de_vida = ponto_de_vida

    def ataque(self, oponente):
        dano = (self.ataque_especial + self.ataque_normal * random.randint(1, 4) - oponente.defesa * random.randint(1, 4))

        if dano < 0:
            dano = 0

        oponente.ponto_de_vida -= dano
        return dano


class Jogador:
    def __init__(self, nome, frota):
        self.nome = nome
        self.frota = frota


class Duelo:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def iniciarBatalha(self):

        while self.jogador1.frota and self.jogador2.frota:

            nave1 = self.jogador1.frota[0]
            nave2 = self.jogador2.frota[0]

            print(f"{nave1.nome} de {self.jogador1.nome} ataca {nave2.nome} de {self.jogador2.nome}")

            nave1.ataque(nave2)

            if nave2.ponto_de_vida <= 0:
                print(f"{nave2.nome} foi destruída!")
                self.jogador2.frota.pop(0)
            else:
                print(f"{self.jogador2.nome} ataca!")
                nave2.ataque(nave1)

                if nave1.ponto_de_vida <= 0:
                    print(f"{nave1.nome} foi destruída!")
                    self.jogador1.frota.pop(0)

        if not self.jogador1.frota:
            print(f"\n{self.jogador2.nome} ganhou!")
        else:
            print(f"\n{self.jogador1.nome} ganhou!")


Naves_jogo = []

Naves_jogo.append(Nave("X-Wing", 8, 12, 6, 20))
Naves_jogo.append(Nave("TIE Fighter", 6, 10, 4, 18))
Naves_jogo.append(Nave("Millenium Falcon", 10, 15, 8, 30))
Naves_jogo.append(Nave("Star Destroyer", 12, 20, 10, 40))
Naves_jogo.append(Nave("Slave_I", 9, 14, 7, 25))
Naves_jogo.append(Nave("A-Wing", 7, 11, 5, 15))
Naves_jogo.append(Nave("Interceptor", 8, 13, 6, 20))
Naves_jogo.append(Nave("Y-Wing", 6, 12, 7, 22))
Naves_jogo.append(Nave("Imperial Shuttl", 5, 8, 9, 35))
Naves_jogo.append(Nave("Rebel Transport", 6, 10, 7, 38))
Naves_jogo.append(Nave("Ebon Hawk", 8, 14, 7, 28))
Naves_jogo.append(Nave("TIE Bomber", 7, 12, 6, 22))
Naves_jogo.append(Nave("ARC-170", 9, 15, 8, 26))
Naves_jogo.append(Nave("Naboo Starfighter", 6, 10, 5, 18))
Naves_jogo.append(Nave("Ghost", 10, 18, 9, 32))
Naves_jogo.append(Nave("TIE Defender", 1, 16, 8, 30))
Naves_jogo.append(Nave("Z-95 Headhunter", 7, 11, 6, 20))
Naves_jogo.append(Nave("U-Wing", 8, 13, 7, 24))
Naves_jogo.append(Nave("E-Wing", 9, 14, 8, 26))
Naves_jogo.append(Nave("Razor Crest", 9, 16, 8, 32))

jogadorUm = Jogador("Ciclano", random.sample(Naves_jogo, 4))
jogadorDois = Jogador("Fulano", random.sample(Naves_jogo, 4))

print(f"Nome do Jogador 1: {jogadorUm.nome}")
print(f"Nome do Jogador 2: {jogadorDois.nome}")

duelo = Duelo(jogadorUm, jogadorDois)
duelo.iniciarBatalha()