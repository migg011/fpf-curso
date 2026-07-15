# Crie uma função que recebe uma lista de números e retorna a soma deles.

def somar(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
entrada = input("qual operacao deseja fazer? ").lower()

if entrada == "soma":
    print(somar(numero1, numero2))
    saida = input("deseja sair? (SIM/NAO): ").lower()
elif entrada == "subtracao":
    print(subtracao(numero1, numero2))
    saida = input("deseja sair? (SIM/NAO): ").lower()
elif entrada == "multiplicacao":
    print(multiplicacao(numero1, numero2))
    saida = input("deseja sair? (SIM/NAO): ").lower()
elif entrada == "divisao":
    if (numero1 == 0) or (numero2 == 0):
        print("impossivel dividir por 0")
        saida = input("deseja sair? (SIM/NAO): ").lower()
    else:
        print(divisao(numero1, numero2))
        saida = input("deseja sair? (SIM/NAO): ").lower()

while saida == "nao":
    numero1 = int(input("digite o primeiro numero: "))
    numero2 = int(input("digite o segundo numero: "))
    entrada = input("qual operacao deseja fazer? ").lower()

    if entrada == "soma":
        print(somar(numero1, numero2))
        saida = input("deseja sair? (SIM/NAO): ").lower()
    elif entrada == "subtracao":
        print(subtracao(numero1, numero2))
        saida = input("deseja sair? (SIM/NAO): ").lower()
    elif entrada == "multiplicacao":
        print(multiplicacao(numero1, numero2))
        saida = input("deseja sair? (SIM/NAO): ").lower()
    elif entrada == "divisao":
        if (numero1 == 0) or (numero2 == 0):
            print("impossivel dividir por 0")
        else:
            print(divisao(numero1, numero2))
            saida = input("deseja sair? (SIM/NAO): ").lower()