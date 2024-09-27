class Coisas:
    def __init__(self,numero1,numero2):
        self.numero1=numero1
        self.numero2=numero2

    def retornar(self):
        soma= self.numero1 + self.numero2
        return soma

c = Coisas(5,6)
