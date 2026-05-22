class Funcionario:
    def __init__(self, nome, salario_base):
        self.__nome = nome
        self.__salario_base = salario_base

    def get_salario(self):
        return self.__salario_base

    def get_nome(self):
        return self.__nome

    def calcular_pagamento(self):
        return self.__salario_base


class Gerente(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    def calcular_pagamento(self):
        return self.get_salario() + 1000


class Estagiario(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    def calcular_pagamento(self):
        return self.get_salario() * 0.8
