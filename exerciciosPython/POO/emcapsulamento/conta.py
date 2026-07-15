class Conta:
    def __init__(self):

        # __ é privado. _ é protegido
        self.__saldo = 0


    # getter -> utilizado para ler um atributo privado
    # permite acessar o valor sem alterar diretamente
    def get_saldo(self):
        return self.__saldo

    # setter -> altera o atributo privaoo, mas de forma controlada
    # aqui ele funciona como um setter, mas com um nome "depositar"
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

#exemplo de uso

conta = Conta()

print(conta.get_saldo())

conta.depositar(500)

print(conta.get_saldo())

conta.sacar(200)

#verificar novamente o saldo da conta via getter

print(conta.get_saldo())