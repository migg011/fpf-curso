# PROBLEMA 2: Jogo de Personagens
# Crie um sistema de personagens para RPG:
#
# Classe base: Personagem com nome, vida, forca e método atacar()
#
# Classes filhas:
#
# Guerreiro: ganha método defender() e atacar() causa dano extra
#
# Mago: ganha mana e método lancar_magia()
#
# Arqueiro: ganha precisao e método atacar_distancia()
#
# Cada classe tem habilidades únicas

class Personagem:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self):
        print(f"{self.nome} atacou! DANO CAUSADO: {self.forca}")

class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome,vida,forca)

    def defender_mais_saude(self):
        print(f"{self.nome}, o guerreiro, se defendeu!")
        self.vida += 10
        print(f"a vida de {self.nome}, aumentou em 10. STATUS VIDA: {self.vida}")


    def atacar(self):

        dano_total = self.forca + 15

        print("o guerreiro da mais DANO! +10 de força!")
        print(f"{self.nome}, o guerreiro, atacou! DANO CAUSADO: {dano_total}")

# Mago: ganha mana e método lancar_magia()

class Mago(Personagem):
    def __init__(self, nome, vida, forca, mana):
        super().__init__(nome, vida, forca)
        self.mana = mana

    def lancar_magia(self):
        if self.mana >= 20:
            self.mana -= 20
            dano_magia = self.forca * 3
            print(f"{self.nome}, o mago, lancou uma magia! DANO CAUSADO: {dano_magia}")
            print(f"magia restante de {self.nome}: {self.mana}")
        else:
            print("magia insuficiente do mano mago!")

# Arqueiro: ganha precisao e método atacar_distancia()

class Arqueiro(Personagem):
    def __init__(self, nome, vida, forca, precisao):
        super().__init__(nome, vida, forca)
        self.precisao = precisao

    def atacar_distancia(self):

        dano_distancia = self.forca + 5

        print(f"{self.nome}, o arqueiro, lancou um ataque a distancia! DANO CAUSADO: {dano_distancia}")

thor = Guerreiro("thor", 100, 20)
doutor = Mago("doutor estranho", 100, 10, 40)
gaviao = Arqueiro("gaviao arqueiro", 100, 15, 100)

thor.atacar()
thor.defender_mais_saude()

doutor.atacar()
doutor.lancar_magia()
doutor.lancar_magia()
doutor.lancar_magia()


gaviao.atacar()
gaviao.atacar_distancia()
