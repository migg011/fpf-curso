class Funcionario:

    def __init__(self, nome_dado, cargo_dado, salario_dado):
        self.nome = nome_dado
        self.cargo = cargo_dado
        self.salario = salario_dado

    def exibir_info(self):
        print(f"funcionarios cadastrado: {self.nome} - {self.cargo} - {self.salario}")

funcionario = []

for i in range(2):
    print(f"usuarios cadastrados ({i}/2)")
    nome = input("digite seu nome: ")
    cargo = input("digite sua cargo: ")
    salario = float(input("digite sua salario: "))

    funcionario.append(Funcionario(nome, cargo, salario))

print(f"usuarios cadastrados (2/2)")

# funcionario_1 = Funcionario(nome, cargo, salario)
# print("nome: ", funcionario_1.nome)
# print("cargo: ", funcionario_1.cargo)
# print("salario: ", funcionario_1.salario)
#
# funcionario_2 = Funcionario(nome, cargo, salario)
# print("nome: ", funcionario_2.nome)
# print("cargo: ", funcionario_2.cargo)
# print("salario: ", funcionario_2.salario)
#
#
# funcionario_1.exibir_info()
# funcionario_2.exibir_info()

for i in funcionario:
    i.exibir_info()
    salario_somados = salario_somados