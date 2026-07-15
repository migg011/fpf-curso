salario_base = float(input("Digite o o seu salario base: "))
gratificação = (salario_base*5) / 100
imposto = (salario_base * 7) / 100

salario_final = (salario_base + gratificação) - imposto

print("seu salario final é de: ", salario_final)