notas = []

for i in range(5):
    codigo_aluno = input("digite o codigo de aluno: ")
    nota = float(input("digite a nota do aluno: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print("quantidade de notas", len(notas))

for n in notas:
        codigo_aluno = n[0]
        nota = n[1]
        print("o CODIGO DO ALUNO é: ", codigo_aluno, "e sua nota é de: ", nota)
