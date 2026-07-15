class Carro:

    quantidade_total = 0

    def __init__(self, marca, modelo, ano, status = False):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.status = status

        Carro.quantidade_total += 1

    def ligar(self):
        if self.status:
            print("o carro ja esta ligado")
        else:
            print("o carro foi ligado")
            self.status = True

    def desligar(self):
        if not self.status:
            print("o carro ja esta desligado")
        else:
            self.status = False
            print("o carro foi desligado")


    def mostrar(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Status: {self.status}")
        print(f"Quantidade de carros: {Carro.quantidade_total} ")

carro1 = Carro("TOYOTA","ECLYPSE", 2008, False)
carro1.mostrar()
carro2 = Carro("BMW","BLINDADO", 2000, True)
carro2.mostrar()
carro1.ligar()
carro2.desligar()
carro1.mostrar()
carro2.mostrar()

#i love labubu
