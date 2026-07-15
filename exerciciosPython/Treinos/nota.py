nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
nota3 = float(input("digite sua terceira nota: "))
resultado = (nota1+nota2+nota3) / 3
print("sua nota final é de:", resultado)
if resultado >= 7:
    print("aprovado")
else:
    print("reprovado")