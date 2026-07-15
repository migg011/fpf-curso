# A classe deve ter um construtor (__init__) que recebe:
# titulo
# autor
# ano_publicacao
# Dentro do construtor, esses valores devem ser guardados nos atributos do objeto.
# Depois, você vai criar dois objetos da classe Livro, com dados de sua escolha.

class Livro:

    def __init__(self,inf_titulo, inf_autor, inf_ano_publicacao):
        self.titulo = inf_titulo
        self.autor = inf_autor
        self.ano = inf_ano_publicacao

    def retorno(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} - Ano da Publicação: {self.ano}"

livros = []

for i in range(2):
    titulo = input("digite o titulo do seu livro: ")
    autor = input("digite o autor do seu livro: ")
    ano = int(input("digite o ano de publicao do seu livro: "))

    livros.append(Livro(titulo, autor, ano))

for i in livros:
    print(i.retorno())