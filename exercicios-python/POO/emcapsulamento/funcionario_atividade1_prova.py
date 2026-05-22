
# Crie uma classe Funcionario com:
# Atributos privados:
# __nome, __salario | Método calcular_salario()
#
# Crie duas classes filhas:
# FuncionarioCLT → salário fixo
# | FuncionarioHorista → salário por hora
#
# O programa deve:
# Ler dados com input
# Criar funcionários em um laço
# Usar polimorfismo para calcular salários
# Mostrar o total da folha de pagamento
#
# Requisitos
# Usar for ou while
# Usar getters
# Usar lista de objetos

class Funcionario:
    def __init__(self, nome):
        self.__nome = nome
        self.__salario = 0

    def calcular_salario(self):
        return self.__salario

    def get_nome(self):
        return self.__nome

class FuncionarioCLT(Funcionario):
    def __init__(self,nome, salario_fixo):
        super().__init__(nome)
        self.__salario_fixo = salario_fixo

    def get_salario_fixo(self):
        return self.__salario_fixo

    def calcular_salario(self):
        return self.__salario

class FuncionarioHorista(Funcionario):
    def __init__(self,nome, salario_hora):
        super().__init__(nome)
        self.__salario_hora = salario_hora
        self.__horas = 0

    def set_horas(self, horas):
        self.__horas = horas

    def calcular_salario(self):
        return self.__salario_hora * self.__horas


funcionarios = []
tela = True

while tela:
    tipo = input("voce é (1) HORISTA ou (2) CLT:  ").lower()
    if tipo == "horista" or tipo == "1":
        nome = input("digite seu nome: ")
        salario_hora = float(input("digite seu salario por hora: "))
        funcionario_adicionado_horista = FuncionarioHorista(nome, salario_hora)

        horas_trabalhadas = float(input("digite o total de horas trabalhadas: "))
        funcionario_adicionado_horista.set_horas(horas_trabalhadas)

        funcionarios.append(funcionario_adicionado_horista)

    elif tipo == "clt" or tipo == "2":
        nome = input("digite seu nome: ")
        salario_fixo = float(input("digite seu salario fixo: "))
        funcionario_adicionado_clt = FuncionarioCLT(nome, salario_fixo)

        funcionarios.append(funcionario_adicionado_clt)

    else:
        print("OPCAO INVALIDA! TENTE NOVAMENTE!")
        continue

    sair = input("deseja adicionar um funcionario? (SIM/NAO): ").lower()
    if sair == "nao":
        tela = False
    elif sair != "sim":
        print("consideramos como sim.")
        print("na proxima digite certo, por favor!")

print("-- FOLHA DE PAGAMENTO --")

total_folha = 0
for funcionario in funcionarios:
        salario = funcionario.calcular_salario()
        total_folha += salario

        print(f"{funcionario.get_nome()}: R$ {salario:.2f}")

print(f"\nTotal da folha de pagamento: R$ {total_folha:.2f}")











