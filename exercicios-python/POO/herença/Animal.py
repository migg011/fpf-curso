class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print(f"{self.nome} faz um som generico")

class Cachorro(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome}, da raca: {self.raca}, esta latindo: AU AU!")

    def mostrar_detalhes(self):
        print(f"nome: {self.nome}, Especie: {self.especie}, Raca: {self.raca}")

class Gato(Animal):
    def __init__(self, nome, especie, cor_pelo, raca):
        super().__init__(nome, especie)
        self.cor_pelo = cor_pelo
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome}, da raca: {self.raca}, esta miando: miau miau!")

    def mostrar_detalhes(self):
        print(f"nome: {self.nome}, Especie: {self.especie}, Cor do pelo: {self.cor_pelo}, Raca: {self.raca}")

cachorro01 = Cachorro("Ducky", "Canino", "Golden Retriever")
print(f"nome herdado: {cachorro01.nome}")
cachorro01.fazer_som()
cachorro01.mostrar_detalhes()

print("\n")

gato01 = Gato("Laura", "Felino", "Branco", "Siames")
print(f"nome herdado: {gato01.nome}")
gato01.fazer_som()
gato01.mostrar_detalhes()


