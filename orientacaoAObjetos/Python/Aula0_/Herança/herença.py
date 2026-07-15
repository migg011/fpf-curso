class Pessoa:
    especie = "Humano"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__documento = None

    def apresentar(self):
        print(f"Ola, eu me chamo {self.nome}!")

class Funcionario(Pessoa):
    taxa_bonus = 0.05

    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario

    def apresentar(self):
        return f"Sou {self.nome}, trabalho como {self._cargo}!"

