class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def consultar(self):
        print("Titular:  ", self.titular)
        print("Saldo:  ", self.saldo)

    def depositar(self):
        valor = float(input("Informe o valor"))
        self.saldo = self.saldo + valor

    def sacar(self):
        valor = float(input("Informe o valor"))
        self.saldo = self.saldo - valor
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
        else:
            print("Não pode")

    def transferir(self, destinatario, valor):
        if valor > 0 and valor < self.saldo:
            self.saldo = self.saldo - valor
            destinatario.depositar(valor)




c1 = Conta("Maria", 1000)
c2 = Conta("Juliana", 800)
c3 = Conta("Carlos", 900)
c4 = Conta("Tania", 1000)
print(c1.titular, c1.saldo)
c1.consultar()
c1.depositar()
c1.consultar()
c1.sacar()
c1.consultar()
"""
caso nao aceita o contrutor criar um vazio tipo c4 = Conta()

"""
