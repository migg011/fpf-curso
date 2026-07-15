#questao 1

lista_numero = [1,2,3,4,5,6,7,8,9,10]
qntd_par = 0
qntd_impar = 0

for numero in lista_numero:
    if numero % 2 == 0:
        qntd_par = qntd_par + numero
    else:
        qntd_impar = qntd_impar + numero

print("a soma dos pares de 1 a 10 é: ",qntd_par)
print("a soma dos impares de 1 a 10 é: ",qntd_impar)

#questao 2

palavra = input("digite uma palavra: ").lower()

qntd_vogais = 0
qntd_consoantes = 0
qntd_espaco = 0

for i in palavra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        qntd_vogais = qntd_vogais + 1
    elif i == " ":
        qntd_espaco += 1
    else:
        qntd_consoantes = qntd_consoantes + 1

print("sua palavra/frase foi: ", palavra)
print("quantidade de vogais: ", qntd_vogais)
print("quantidade de consoantes: ", qntd_consoantes)
print("quantidade de espacos: ", qntd_espaco)

#questao 3

quantidade_funcionario = int(input("digite quantos funcionarios deseja adicionar: "))

funcionarios = []

for i in range(quantidade_funcionario):

    funcionario_novo = {}

    print(f"{i+1}¨ funcionario")
    funcionario_novo["nome"] = input("digite seu nome: ")
    funcionario_novo["sexo"] = input("digite seu sexo (M / F): ").lower()
    funcionario_novo["salario"] = float(input("digite seu salario: "))

    funcionarios.append(funcionario_novo)

soma_homem = 0
soma_mulher = 0

for funcionario in funcionarios:
    if funcionario["sexo"] == 'm':
        soma_homem += funcionario["salario"]
    elif funcionario["sexo"] == 'f':
        soma_mulher += funcionario["salario"]

print("\ntotal de funcionarios adicionados foi de: ", quantidade_funcionario)
print("a soma total dos salarios homens é: ",soma_homem)
print("a soma total dos salarios mulheres é: ",soma_mulher)