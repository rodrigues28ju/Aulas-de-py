class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def consultar(self):
        print("Titular:  ", self.titular)


c1 = Conta("Maria", 1000)
c2 = Conta("Juliana", 800)
c3 = Conta("Carlos", 900)
c4 = Conta("Tania", 1000)
print(c1.titular, c1.saldo)
c1.consultar()
"""
caso nao aceita o contrutor criar um vazio tipo c4 = Conta()

"""
