class Cachorro:

    def __init__(self, inf_nome, inf_raca, inf_idade):
        self.nome = inf_nome
        self.raca = inf_raca
        self.idade = inf_idade

    def result(self):
        return f"nome : {self.nome}, raça: {self.raca}, idade: {self.idade}"

cachorro_1 = Cachorro("Dogets", "Vira-Lata", "1 ano e 4 meses")
cachorro_2 = Cachorro("Nuggets", "Shih Tzu", "3 anos")

print(cachorro_1.result())
print(cachorro_2.result())