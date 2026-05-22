# Classe
#
# Alarme
#
# Atributos (__init__)
#
# self.senha (int), self.armado (bool, inicializa em False),
# self.disparado (bool, inicializa em False)
#
# Método 1: Ação
#
# armar(senha_tentativa): Se senha_tentativa for igual a
# self.senha, muda self.armado para True e imprime o
# estado.
#
# Método 2: Ação
#
# disparar(): Se self.armado for True, muda self.disparado
# para True e imprime "ALARME ATIVADO! POLÍCIA
# CHAMADA!".
#
# Método 3: Estado
#
# desarmar(senha_tentativa): Se a senha_tentativa for igual
# a self.senha, muda self.armado e self.disparado para
# False.

class Alarme:
    def __init__(self, senha):
        self.senha = senha
        self.armado = False
        self.disparado = False

    def armar(self,senha_tentativa):
        if senha_tentativa == self.senha:
            self.armado = True
            print("alarme armado")

    def disparar(self):
        if self.armado:
            self.disparado = True
            print("ALARME ATIVADO! POLÍCIA CHAMADA!")

    def desarmar(self, senha_tentativa):
        if senha_tentativa == self.senha:
            self.armado = False
            self.disparado = False
            print("o alarme foi desativado")

alarme01 = Alarme(123)
alarme01.armar(123)
alarme01.disparar()
alarme01.desarmar(123)

