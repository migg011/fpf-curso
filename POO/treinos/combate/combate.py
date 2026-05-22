from personagem import Guerreiro, Mago

guerreiro = Guerreiro("Aragorn")
mago = Mago("Gandalf")

print(guerreiro.get_vida())
mago.lancar_magia(guerreiro)
print(guerreiro.get_vida())