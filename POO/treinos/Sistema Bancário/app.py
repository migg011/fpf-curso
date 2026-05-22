# Arquivo 2: app.py
# Crie duas contas: "Conta A" com R$ 500 e "Conta B" com R$ 100.

# Tente transferir R$ 200 da A para a B.

# Tente transferir R$ 1000 da A para a B (deve dar erro de saldo).

# Exiba o saldo final das duas contas.

from banco import Conta

conta1 = Conta("Conta A", 500)
conta2 = Conta("Conta B", 100)

conta1.transferir(500, conta2)
conta1.transferir(1000, conta2)

print(conta1.get_saldo())
print(conta2.get_saldo())
