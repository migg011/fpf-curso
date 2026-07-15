class Cachorro:

    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        return f"{self.nome} o cachorro está latindo: 'AU AU'"

    def fazer_aniversario(self):
        self.idade += 1 # Modifica o atributo 'idade'
        return f"Parabéns! {self.nome} agora tem {self.idade} anos. "


    def apresemtar(self):
        return f"Olá, eu sou {self.nome}. minha raça é {self.raca} de {self.idade} anos."

dog_a = Cachorro("Max", "Golden Retriever", 5)
dog_b = Cachorro("Luna", "Poodle", 2)

print(dog_a.apresemtar())
print(dog_a.latir())

print(dog_b.apresemtar())
print(dog_b.latir())


print(dog_a.fazer_aniversario())
print(dog_a.apresemtar())