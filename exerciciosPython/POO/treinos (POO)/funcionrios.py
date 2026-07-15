
# Crie uma classe Funcionario com:
# Atributos privados: __nome, __salario | Método calcular_salario()

# Crie duas classes filhas: FuncionarioCLT → salário fixo | FuncionarioHorista → salário por hora
# O programa deve:

# Ler dados com input
# Criar funcionários em um laço
# Usar polimorfismo para calcular salários
# Mostrar o total da folha de pagamento
# Requisitos
# Usar for ou while
# Usar getters
# Usar lista de objeto

class Funcionario:
    def __init__(self, nome):
        self.__nome = nome
        self.__salario = 0

    def calcular_salario(self):
        return self.__salario

    def get_nome(self):
        return self.__nome

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario_fixo):
        super().__init__(nome)
        self.__salario_fixo = salario_fixo

    def calcular_salario(self):
        return self.__salario_fixo

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, salario_hora):
        super().__init__(nome)
        self.__salario_hora = salario_hora
        self.__horas = 0

    def set_horas(self, horas):
        self.__horas = horas

    def calcular_salario(self):
        return self.__salario_hora * self.__horas

funcionarios = []

total_valor = 0

while True:
    print("TIPO FUNCIONARIO")
    print(" 1 - CLT")
    print(" 2 - HORISTA")
    print(" QUALQUER OUTRA TECLA - SAIR")
    tipo = input("escolha sua opção: ")

    if tipo == "1":
        nome = input("digite seu nome: ")
        salario_fixo = float(input("digite seu salario fixo: "))

        funcionarioClt = FuncionarioCLT(nome, salario_fixo)

        funcionarios.append(funcionarioClt)

    elif tipo == "2":
        nome = input("digite seu nome: ")
        salario_hora = float(input("quanto que voce ganha por hora? "))
        funcionarioHorista = FuncionarioHorista(nome,salario_hora)

        horas_trabalhadas = float(input("quantas horas voce trabalhou? "))
        funcionarioHorista.set_horas(horas_trabalhadas)

        funcionarios.append(funcionarioHorista)

    else:
        print("saindo...")
        break

print("FUNCIONARIOS CADASTRADOS:")
for funcionario in funcionarios:
    salario = funcionario.calcular_salario()
    total_valor += salario
    print(f"nome: {funcionario.get_nome()}, salario total: {salario}")

print("FOLHA DE PAGAMENTO: ")
print(f"R$ {total_valor}")