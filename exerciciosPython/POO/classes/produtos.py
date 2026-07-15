# Crie uma classe Produto que representa um item em um estoque.
# A classe deve ter:
# nome
# preco (número decimal)
# quantidade (inteiro)
# Crie um método chamado valor_total() que calcula e retorna preco * quantidade.
# Crie um método chamado detalhes() que retorna uma string formatada com nome, preço, quantidade e valor total.
# Crie pelo menos 2 produtos (pode ser com input ou fixos).
# Exiba os detalhes de cada produto.

class Produto:

    def __init__(self, nome_dado, preco_dado, quantidade_dado):
        self.nome = nome_dado
        self.preco = preco_dado
        self.quantidade = quantidade_dado

    def valor_total(self):
        return self.preco * self.quantidade

    def detalhes(self):
        print(f"nome do produto: {self.nome}\n"
              f"preco: {self.preco}\n"
              f"quantidade: {self.quantidade}\n"
              f"valor total: R${self.valor_total()}")

produtos = []

for i in range(2):
    print(f"produtos adicionados ({i}/2)")
    nome = input("digite o nome do produto: ")
    preco = float(input("digite o preco do produto: "))
    quantidade = int(input("digite a quantidade: "))

    produtos.append(Produto(nome, preco, quantidade))

print(f"produtos adicionados (2/2)")

for i in produtos:
    i.detalhes()

