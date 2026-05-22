# A nave Endurance precisa calcular a quantidade total de combustível necessária para várias
# missões de reconhecimento em sistemas estelares diferentes. Cada missão exige uma quantidade
# específica de unidades de combustível.

# Crie uma função em Python chamada calcula_combustivel que receba:
# 1. Um argumento posicional obrigatório: missoes_base (o número de missões fixas, por exemplo,
# 2).
# 2. Um número variável de argumentos usando *args: gastos_adicionais
# A função deve:
#
#  Considerar que cada missão fixa (missoes_base) gasta 100 unidades de combustível.
#
#  Usar um laço de repetição para somar todos os valores em gastos_adicionais.

#  Calcular o total geral (combustível das missões fixas + gastos adicionais).
#  Imprimir (usando print) o total de combustível necessário.
#  calcula_combustivel(2, 50, 25, 10)

def calcula_combustivel(missoes_base, *gastos_adicionais):

    total_combustivel = missoes_base * 100
    soma_valores = 0

    for gasto in gastos_adicionais:
         soma_valores += gasto

    total_geral = total_combustivel + soma_valores

    return f"o total de combustiveis necessario é de: {total_geral}"

print(calcula_combustivel(2, 50, 25, 10))