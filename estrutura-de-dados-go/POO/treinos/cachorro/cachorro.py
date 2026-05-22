class Cachorro:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    
    def latir(self):
        return 0 
    
    def apresentar(self):
        print (f"meu nome é: {self.__nome}, tenho {self.__idade} anos de idade!")

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade

class CachorroQueVoa(Cachorro):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.__voa = False

    def latir(self):        
        if self.__voa:
            print(f"o {self.get_nome()}, que voa, latiu: RUF RUF")
        else:
            print(f"o {self.get_nome()}, que NAO VOA, latiu: RUF RUF")

    def consegue_voar(self):
        if self.__voa:
            print(f"o {self.get_nome()} consegue voar nao sei como! ")
        else: 
            print(f"o {self.get_nome()} nao consegue voar, mt buxa")
    
    def set_voa(self, voar):
        self.__voa = bool(voar)
        print(f"agora o {self.get_nome()} VOA!\n")

class CachorroLaser(Cachorro):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.__laser = False
    
    def latir(self):        
        if self.__laser:
            print(f"o {self.get_nome()}, que solta laser pelos olhos, latiu: RUF RUF")
        else:
            print(f"o {self.get_nome()}, que NAO solta laser pelos olhos, latiu: RUF RUF")
    
    def consegue_laser(self):
        if self.__laser:
            print(f"o {self.get_nome()} consegue soltar laser pelos olhos nao sei como! ")
        else: 
            print(f"o {self.get_nome()} nao consegue soltar laser pelo olho, mt fraco esse buxa")
    
    def set_laser(self, laser):
        self.__laser = bool(laser)
        print(f"agora o {self.get_nome()} consegue soltar LASER!\n")

        

Catioros = []

quantidade = int(input(f"quantos catioros deseja adicionar: "))

for i in range(quantidade):
    print("--MENU DE CACHORROS--")
    print(" 1 - CATIORO QUE VOA ")
    print(" 2 - CATIORO QUE SOLTA LASER PELOS OLHOS ")
    opcao = int(input("digite sua opcao: "))

    match opcao:
        case 1:
            nome = input("qual é o nome do cachorro:  ")
            idade = int(input("idade: "))

            dog = CachorroQueVoa(nome, idade)
            Catioros.append(dog)
        case 2:
            nome = input("qual é o nome do cachorro:  ")
            idade = int(input("idade: "))

            dog = CachorroLaser(nome, idade)
            Catioros.append(dog)
        case _:
            print("nao existe essa opcao")

for cachorro in Catioros:
    cachorro.apresentar()
    cachorro.latir()



    