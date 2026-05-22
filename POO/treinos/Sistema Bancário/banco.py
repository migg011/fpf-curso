# Classe Conta:

# __init__: Nome do titular e saldo (privado __saldo).

# Método get_saldo(): Para apenas ler o valor.

# Método depositar(valor): Soma ao saldo.

# Método sacar(valor): Lógica importante: Só subtrai se o saldo for suficiente. Se não for, printa "Saldo insuficiente".

# Método transferir(valor, destino): Aqui está o pulo do gato. Este método deve:

# Tentar sacar da própria conta.

# Se o saque der certo, chamar o método destino.depositar(valor).

class Conta:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            print("saldo insuficiente")
            return False

    def transferir(self, valor, destino):
        if self.sacar(valor):
            destino.depositar(valor)
            print("transferencia concluida")
