# Leia o salário, valor do empréstimo e número de parcelas
#
# Calcule a parcela mensal (valor / parcelas)
#
# Aprove o empréstimo se:
#
# Parcela ≤ 30% do salário E número de parcelas ≤ 24
#
# Caso contrário, reprove
#
# Dica: Você vai precisar calcular 30% do salário para fazer a comparação.

salario = float(input("digite seu salario: "))
emprestimo = float(input("digite o valor do emprestimo: "))
n_parcelas = float(input("digite o numero de parcelas: "))

parcela_mensal = (emprestimo / n_parcelas)
porcentagem_salarial = (salario * 30) / 100

print(parcela_mensal)
print(porcentagem_salarial)

if parcela_mensal <= porcentagem_salarial and n_parcelas <= 24:
    print("situação: aprovada")
else:
    print("situação: recusada")