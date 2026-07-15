# Leia 3 notas de um aluno (0-10)
#
# Calcule a média
#
# Atribua conceito:
#
# A: média ≥ 9.0
#
# B: 7.0 ≤ média < 9.0
#
# C: 5.0 ≤ média < 7.0
#
# D: média < 5.0

def media(a, b, c):
    return (a + b + c) / 3

num1 = float(input("digite sua primeira nota: "))
num2 = float(input("digite sua segunda nota: "))
num3 = float(input("digite sua terceira nota: "))
valor_media = media(num1,num2,num3)

print(valor_media)

if valor_media >= 9:
    print("resultado: A")
elif 7 <= valor_media < 9:
    print("resultado: B")
elif 5 <= valor_media < 7 :
    print("resultado: C")
elif valor_media < 5:
    print("resultado: D")

