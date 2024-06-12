import self
class Contacorrente:
    def __init__(self,numeroconta: int, nome: str, saldo: float):
        self.numeroconta = int(numeroconta)
        self.nome = str(nome)
        self.saldo = float(saldo)

    def alterarnome(self,nome):
        self.nome = str(nome)

    def deposito(self,saldo):
     self.saldo += float(saldo)

    def saque(self,saldo):
        self.saldo -= float(saldo)

    def mostrarconta(self):
        print(f'numeroconta: {self.numeroconta}, nome: {self.nome}, saldo: {self.saldo}')

contal = Contacorrente('000134','ana','400')
contal.mostrarconta()
contal.alterarnome('ana silva')
contal.mostrarconta()
contal.deposito(200)
contal.mostrarconta()




