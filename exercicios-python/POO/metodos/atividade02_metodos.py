 
# Classe
# 
# PlayerMusical
# 
# Atributos (__init__)
# 
# self.volume (int, inicializa em 50), self.tocando (bool,
# inicializa em False)
# 
# Método 1: Estado
# 
# play(): Se self.tocando for False, muda para True e
# imprime "Música iniciada.".
# 
# Método 2: Estado
# 
# pause(): Se self.tocando for True, muda para False e
# imprime "Música pausada.".
# 
# Método 3: Ação
# 
# aumentar_volume(passos): Adiciona passos ao
# self.volume. Garanta que o volume nunca ultrapasse 100.

class PlayerMusical:

    def __init__(self):
        self.volume = 50
        self.tocando = False

    def play(self):
        if not self.tocando:
            self.tocando = True
            print("musica iniciada")

    def pause(self):
        if self.tocando:
            self.tocando = False
            print("musica pausada")

    def aumentar_volume(self, passos):

        self.volume += passos

        if self.volume > 100:
            self.volume = 100
            print(f"volume no maximo")
        else:
            print(f"foi aumentado {passos} no volume, volume atual: {self.volume}")

musica01 = PlayerMusical()
musica01.play()
musica01.pause()
musica01.play()
musica01.aumentar_volume(50)
musica01.aumentar_volume(1)
