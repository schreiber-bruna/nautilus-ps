
class Auv:
    def __init__(self, nome: str, ano: int, numero_thursters: int):
        self.__nome =nome
        self.__ano = ano
        self.__numero_thursters = numero_thursters
    def get_nome(self):
        return self.__nome
    def get_ano(self):
        return self.__ano
    def get_numero_thursters(self):
        return self.__numero_thursters

robo = Auv(nome = "BrHUE", ano = 2020, numero_thursters = 6)
robo1 = Auv(nome = "Lua", ano = 2016, numero_thursters = 8 )
robos = [robo, robo1]

class Nautilus:
    def __init__(self, robos_lista):
        self.robos_lista = robos_lista
    
    def exibirtodos(self):
        for r in self.robos_lista:
            print(r.get_nome(), r.get_ano(), r.get_numero_thursters())

    def um_deles(self):
        qual = int(input("Digite 1 para o acessar as informações do BrHUE ou 2 para as informações do Lua:\n"))
        if qual==1:
            print(self.robos_lista[0].get_nome(), self.robos_lista[0].get_ano(), self.robos_lista[0].get_numero_thursters())

        elif qual == 2:
            print(self.robos_lista[1].get_nome(), self.robos_lista[1].get_ano(), self.robos_lista[1].get_numero_thursters())
        
        else:
            print("Opção inválida\n")
    
    def rank(self):
        a = self.robos_lista[0]
        b = self.robos_lista[1]
        if a.get_ano()>b.get_ano():
            print("1º: ", a.get_nome())
            print("2º: ", b.get_nome())
        else:
            print("1º: ", b.get_nome())
            print("2º: ", a.get_nome())
        


nautilus = Nautilus(robos_lista=robos)
nautilus.exibirtodos()
nautilus.um_deles()
nautilus.rank()