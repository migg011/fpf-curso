lista = ["carro", 92, True, 4.14]
print(lista)
print(type(lista))

tupla = ("carro", 92, True, 4.14)
print(tupla)
print(type(tupla))

dicionario = {"nome": "carro", "logica": True, "numero": 2}
print(dicionario)
print(type(dicionario))

nome = "miguel"

for letras in nome:
    if letras == 'm' or letras == 'i':
        continue
    print(letras)