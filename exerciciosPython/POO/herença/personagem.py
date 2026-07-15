class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

class Heroi(Personagem):
    def __init__(self,nome, vida, habilidade):
        super().__init__(nome,vida)
        self.habilidade = habilidade

class Vilao(Personagem):
    def __init__(self, nome, vida, poder):
        super().__init__(nome,vida)
        self.poder = poder

def atacar(personagem):
    print(f"{personagem.nome} esta atacando!")

heroi01 = Heroi("super-human", 98, "raio-lazer")
vilao01 = Vilao("bizarro", 80, "bizarro")

atacar(heroi01)
atacar(vilao01)
