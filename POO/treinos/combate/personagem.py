# Classe Mago:

# __init__: Nome.

# lancar_magia(self, alvo): O parâmetro alvo será o objeto Guerreiro. Dentro deste método, você deve chamar alvo.receber_dano(25).

class Guerreiro:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def get_vida(self):
        return self.vida

    def receber_dano(self, quantidade):
        self.vida -= quantidade


class Mago:
    def __init__(self, nome):
        self.nome = nome

    def lancar_magia(self, alvo):
        print(f"{self.nome} lança magia em {alvo.nome}!")
        alvo.receber_dano(25)
