
# Crie uma classe Pagamento com:
#
# Método calcular_valor()
#
# Crie classes filhas:
#
# PagamentoCartao
#
# PagamentoPix
#
# PagamentoBoleto
#
# Cada forma aplica regras diferentes (taxa, desconto, etc.).
#
# O programa deve:
#
# Ler dados de pagamento com input
#
# Calcular valores usando polimorfismo
#
# Processar vários pagamentos em um laço

class Pagamento:
    def __init__(self, valor):
        self.__valor = valor

    def calcular_valor(self):
        return self.__valor

    def get_valor(self):
        return self.__valor

class PagamentoCartao(Pagamento):
    def __init__(self,valor):
        super().__init__(valor)

    def calcular_valor(self):
        return self.get_valor() * (1 + 5/100)

class PagamentoPix(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def calcular_valor(self):
        return self.get_valor() * (1 - 5/100) # 5% de desconto

class PagamentoBoleto(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def calcular_valor(self):
        return self.get_valor() #sem nada

produtos = []

quantidade = int(input("quantos produtos deseja comprar? "))

for i in range(quantidade):
    valor = float(input(f"digite o valor do {i + 1} produto"))
    print("forma de pagamento")
    print(" 1 - CARTAO")
    print(" 2 - PIX")
    print(" 3 - BOLETO")
    tipo_pagamento = input("digite a forma de pagamento:")

    if tipo_pagamento == "1":
        pagamento = PagamentoCartao(valor)
        produtos.append(pagamento)
    elif tipo_pagamento == "2":
        pagamento = PagamentoPix(valor)
        produtos.append(pagamento)
    elif tipo_pagamento == "3":
        pagamento = PagamentoBoleto(valor)
        produtos.append(pagamento)


total_valor = 0

for produto in produtos:
    valor_final = produto.calcular_valor()
    total_valor += valor_final

print("valor total: ", total_valor)
