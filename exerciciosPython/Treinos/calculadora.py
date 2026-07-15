num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))
action = input("digite a operação que deseja fazer: ")

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

if action == "soma":
    print("A soma de {:.0f} e {:.0f} é {:.0f}".format(num1, num2, soma))

elif action == "subtracao":
    print("A subtracao de {:.0f} e {:.0f} é {:.0f}".format(
        num1, num2, subtracao))

elif action == "divisao":
    if num2 == 0:
        print("Erro")
    else:
        divisao = num1 / num2
        print("A divisao de {:.2f} e {:.2f} é {:.2f}".format(
            num1, num2, divisao))

elif action == "multiplicacao":
    print("A multiplicacao de {:.0f} e {:.0f} é {:.0f}".format(
        num1, num2, multiplicacao))

else:
    print("erro")
