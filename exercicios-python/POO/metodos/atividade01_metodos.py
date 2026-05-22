# Programador
#
# Atributos (__init__)
#
# self.nome (str), self.linguagem (str), self.produtividade (int,
# inicializa como 100)
#
# Método 1: Ação
#
# codificar(horas): Diminui self.produtividade em 5 pontos
# por horas codificadas e imprime a atividade.
#
# Método 2: Ação
#
# tomar_cafe(): Aumenta self.produtividade em 15 pontos e
# imprime que a produtividade foi restaurada.
#
# Método 3: Estado
#
# verificar_produtividade(): Retorna o nível atual de
# self.produtividade.

class Programador:

    def __init__(self, nome, linguagem):
        self.nome = nome
        self.linguagem = linguagem
        self.produtividade = 100

    def codificar(self,horas):
        total_gasto = horas * 5
        self.produtividade -= total_gasto
        print(f"a atividade gastou, em {horas} horas, {total_gasto} de produtividade")

    def tomar_cafe(self):
        self.produtividade += 15
        print(f"sua produtividade foi restaurada!")

    def verificar_produtividade(self):
        print(f"nivel atual da produtividade, do(a) {self.nome}, é de: {self.produtividade}")

programador01 = Programador("miguel", "python")
programador01.verificar_produtividade()
programador01.codificar(6)
programador01.verificar_produtividade()
programador01.tomar_cafe()
programador01.verificar_produtividade()

#i love labubu



