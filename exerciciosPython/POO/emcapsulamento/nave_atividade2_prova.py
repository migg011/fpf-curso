# Crie uma classe VeiculoEspacial com:
# Atributo privado __combustivel

# Método consumir_combustivel()
# Crie classes filhas:

# NaveCarga
# NaveExploracao
# Cada nave consome combustível de forma diferente.

# O programa deve:
# Criar várias naves usando input
# Consumir combustível em um laço
# Mostrar o combustível restante

























quantidade = int(input("quantas naves deseja adicionar? "))

for i in range(quantidade):
    print(" 1 :NaveCarga")
    print(" 2 :NaveExploracao")
    tipo = input("que tipo de nave é: ")

    if tipo == "1":
        combustivel = NaveCarga()
    elif tipo == "2":
        combustivel = NaveExploracao()
    else:
        print("tipo de nave invalida!")


