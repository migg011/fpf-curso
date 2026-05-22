

from POO.treinos.empresa.empresa import Gerente
from POO.treinos.empresa.empresa import Estagiario

equipe = []
opcoes = ["TABELA DE FUNCIONARIOS: ", " 1 - GERENTE ", " 2 - ESTAGIARIO"]

while True:
    for opcao in opcoes:
        print(opcao)
    opcao = int(input("digite sua opcao: "))

    nome = input("digite seu nome: ")
    salario = float(input("digite seu salario base: "))

    match opcao:
        case 1:
            funcionario = Gerente(nome, salario)
            equipe.append(funcionario)

        case 2:
            funcionario = Estagiario(nome, salario)
            equipe.append(funcionario)

    sair = input("deseja adicionar mais um funcionario? (SIM / NAO): ").lower()
    if sair == "sim":
        continue
    elif sair == "nao":
        break
    else:
        print("entendemos que voce quis sair")
        break


for funcionario in equipe:
    print(f"Funcionario: {funcionario.get_nome()}, Salario: {funcionario.calcular_pagamento()}")
