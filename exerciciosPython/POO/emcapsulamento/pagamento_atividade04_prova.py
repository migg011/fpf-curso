# # Crie uma classe Pagamento com:
# # Método calcular_valor()
# # Crie classes filhas:
# # PagamentoCartao
# # PagamentoPix
# # PagamentoBoleto
#
# # Cada forma aplica regras diferentes (taxa, desconto, etc.).
#
# # O programa deve
#
# # Ler dados de pagamento com input
# # Calcular valores usando polimorfismo
# # Processar vários pagamentos em um laço
#
# class Pagamento:
#     def __init__(self, valor_base):
#         self.valor_base = valor_base
#
#     def calcular_valor(self):
#         return self.valor_base
#
# class PagamentoCartao(Pagamento):
#     def __init__(self, valor_base):
#         super().__init__(valor_base)
#         self.__taxa = 0.05
#
#     def calcular_valor(self):
#         return self.valor_base * (1 + self.__taxa)
#
# class PagamentoPix(Pagamento):
#     def __init__(self, valor_base):
#         super().__init__(valor_base)
#         self.__desconto = 0.10
#
#     def calcular_valor(self):
#         return self.valor_base * (1 - self.__desconto)
#
# class PagamentoBoleto(Pagamento):
#     def __init__(self, valor_base):
#         super().__init__(valor_base)
#         self.__desconto = 0.05
#
#     def calcular_valor(self):
#         return self.valor_base * (1 - self.__desconto)
#
# quantidade = int(input("quantos produtos que voce vai comprar? "))
#
# produtos = []
#
# for i in range(quantidade):
#     valor = float(input(f"digite o preco do {i + 1}¨ produto: "))
#
#     print("-- TIPO DE PAGAMENTO --")
#     print("1 - CARTAO")
#     print("2 - PIX")
#     print("3 - BOLETO")
#     tipo = input("digite a forma de pagamento: ")
#
#     if tipo == "1":
#         pagamento = PagamentoCartao(valor)
#         print("CARTAO: 5% de taxa")
#     elif tipo == "2":
#         pagamento = PagamentoPix(valor)
#         print("PIX: 10% de desconto")
#     elif tipo == "3":
#         pagamento = PagamentoBoleto(valor)
#         print("BOLETO: 5% de desconto")
#     else:
#         print("forma de pagamento invalido!")
#         break
#
#     produtos.append(pagamento)
#
# valor_total = 0
#
# for produto in produtos:
#     valor_total_produto = produto.calcular_valor()
#     valor_total += valor_total_produto
#
# print(f"\no valor total da compra é de {valor_total}")
#
#
#
#
