salario = float(input("digite seu salario para verificarmos: "))
if salario >= 1600 and salario <= 2000:
    print("programador junior")
elif salario > 2000 and salario <= 5000:
    print("programador pleno")
elif salario > 5000 and salario <= 9999:
    print("programador senior")
elif salario >= 10000:
    print("programador master")
else:
    print("voce é buxa ainda")