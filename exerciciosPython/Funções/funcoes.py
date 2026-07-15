# def calcular_imposto(valor):
#     ir = valor * 0.275
#     iss = valor * 0.05
#     csll = valor * 0.0375
#     pis = valor * 0.03
#     return ir + iss + csll + pis
#
# print(calcular_imposto(1000))
#
# print(calcular_imposto(valor = 1000))
#
# def calcular_imposto(valor,perc_ir):
#     ir = valor * perc_ir
#     iss = valor * 0.05
#     csll = valor * 0.0375
#     pis = valor * 0.03
#     return ir + iss + csll + pis
#
# print(calcular_imposto(1000, 0.275))

# def calcular_imposto(valor, *args):
#
#     total_imposto = 0
#
#     for item in args:
#         total_imposto += valor * item
#     return total_imposto
#
# print(calcular_imposto(1000, 0.275, 0.05, 0.0375, 0.03))

# Crie uma função que recebe o valor total de uma compra e vários percentuais de desconto (em decimal).
# A função deve aplicar os descontos um após o outro (cada desconto sobre o valor já descontado) e retornar o valor final.
#
# Exemplo de uso: calcular_valor_final(1000, 0.1, 0.05, 0.02)
# Cálculo: Primeiro desconto de 10%, depois 5% sobre o resultado, depois 2% sobre o resultado.

# def calculo_valor_final(valor, *descontos):
#     total_valor = valor
#
#     for i in descontos:
#         total_valor = total_valor - (total_valor * i)
#     return total_valor
#
# print(calculo_valor_final(1000, 0.1, 0.5, 0.1, 0.15))

# "Calcular salário líquido com vários descontos percentuais (todos sobre o bruto)"
#
# Exemplo: salario_liquido(5000, 0.11, 0.08, 0.015)

def salario_liquido(valor, *desc_percentuais):

    salario_total = valor

    for i in desc_percentuais:
        salario_total = salario_total - (salario_total * i)

    return salario_total

print(salario_liquido(5000, 0.11, 0.08, 0.015))

