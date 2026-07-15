# CLASSE BASE COM ATRIBUTO PRIVADO
class VeiculoEspacial:
    def __init__(self):
        self.__combustivel = 100  # PRIVADO com __

    def consumir_combustivel(self):
        return 0

    # GETTER para ver o combustível
    def get_combustivel(self):
        return self.__combustivel

    # SETTER para alterar o combustível
    def set_combustivel(self, novo_valor):
        self.__combustivel = novo_valor


# CLASSE FILHA 1
class NaveCarga(VeiculoEspacial):
    def consumir_combustivel(self):
        atual = self.get_combustivel()  # usa GETTER
        self.set_combustivel(atual - 30)  # usa SETTER

# CLASSE FILHA 2
class NaveExploracao(VeiculoEspacial):
    def consumir_combustivel(self):
        atual = self.get_combustivel()  # usa GETTER
        self.set_combustivel(atual - 10)  # usa SETTER

naves = []

print("=== CADASTRO DE NAVES ===")
while True:
    print("\n1 - Nave Carga (consome 30)")
    print("2 - Nave Exploração (consome 10)")
    print("3 - Parar cadastro")

    opcao = input("Escolha: ")

    if opcao == "3":
        break

    if opcao == "1":
        nave = NaveCarga()
        naves.append(nave)
        print("✓ Nave de Carga adicionada!")

    elif opcao == "2":
        nave = NaveExploracao()
        naves.append(nave)
        print("✓ Nave de Exploração adicionada!")

    else:
        print("✗ Opção inválida!")

for nave in naves:
    nave.consumir_combustivel()  # Polimorfismo!
    print(f"Combustível: {nave.get_combustivel()}")  # usa GETTER

print("\n=== COMBUSTÍVEL FINAL ===")
for i, nave in enumerate(naves, 1):
    print(f"Nave {i}: {nave.get_combustivel()} de combustível")  # usa GETTER