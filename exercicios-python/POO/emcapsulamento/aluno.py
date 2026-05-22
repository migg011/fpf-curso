class Aluno:
    def __init__(self, nome, nota):
        self.__nome = nome
        self.__nota = nota

    def get_nota(self):
        return self.__nota

    def get_nome(self):
        return self.__nome

    def set_nota(self, valor):
        if valor >= 0 and valor <= 10:
            self.__nota = valor
        else:
            print("nota invalida")

aluno01 = Aluno("sei la quem", 6)

print(aluno01.get_nota())

aluno01.set_nota(11)

print(aluno01.get_nota())

aluno01.set_nota(10)

print(aluno01.get_nota())

