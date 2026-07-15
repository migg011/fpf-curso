class Produto():
    def __init__(self, preco):

        self.__preco = preco

    def get_preco(self):
        return self.__preco

    def set_preco(self, valor):
        if valor >= 0:
            self.__preco += valor
        else:
            print("preco invalidado")

produto01 = Produto(300)
print(produto01.get_preco())

produto01.set_preco(-1)

print(produto01.__preco())



