"""
Temperaturas na faixa ESTÁVEL: entre 150 e 200, INCLUSIVE
Ou seja: temperatura >= 150 E temperatura <= 200

Dados: [145, 160, 195, 210, 150, 200, 155]
Esperado: 5 (160, 195, 150, 200, 155)
"""

def temperaturas_estaveis(temperaturas):

    contador = 0

    for temp in temperaturas:
        if temp >= 150 and temp <= 200:
            contador = contador + 1
    return contador

print(temperaturas_estaveis([145, 160, 195, 210, 150, 200, 155]))