# Algoritmo 1: Cálculo de IMC e Classificação
# Desenvolva um programa que:
#
# Leia o peso (kg) e altura (m) de uma pessoa
#
# Calcule o IMC (peso / altura²)
#
# Classifique conforme:
#
# Abaixo do peso: IMC < 18.5
#
# Peso normal: 18.5 ≤ IMC < 25
#
# Sobrepeso: 25 ≤ IMC < 30
#
# Obesidade: IMC ≥ 30

def imc(a, b):
    return a / (b * b)

peso = float(input("digite seu peso (em kg): "))
altura = float(input("digie sua altura (em metros): "))
valor_imc = imc(peso,altura)

print(f"seu imc é de: {valor_imc:.2f}")

if valor_imc < 18.5:
    print("abaixo do peso")
elif 18.5 <= valor_imc <= 25:
    print("peso normal")
elif 25 <= valor_imc <= 30:
    print("sobrepeso")
elif valor_imc > 30:
    print("obesidade")