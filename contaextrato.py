class Clienteconta:
    def __init__(self, nome, telefone, numero, saldo, limite):
        self.nome = str(nome)
        self.telefone = str(telefone)
        self.numero = str(numero)
        self.saldo = float(saldo)
        self.limite = float(limite)
        #inicia o extrato
        self.extrato = []
    def saque(self, valor):
        if valor < (self.saldo + self.limite):
            self.saldo += valor
        # adcionar ao extrato
            self.extrato.append('-saque' + str(valor))
            return valor
        else:
            print('Saldo insuficiente')
    def deposito(self, valor):
        self.saldo += valor
        #adcionar extrato
        self.extrato.append('+ depósito:' + str(valor))
    def historico(self):
        print('----Extrato-----')
        print('conta',self.numero+'/n')
        for i in self.extrato:
            print(i + '/n')
        print('saldo:',self.saldo)
        print('limite:',self.limite)
        print('disponivel:', self.saldo + self.limite)
    def mostracliente(self):
        print(f'nome: {self.nome} telefone {self.telefone} numero {self.numero} saldo: {self.saldo} limite: {self.limite}')
teste = Clienteconta('ana', '0000000000','10028', '100.00', '3000.00')
teste.mostracliente()
teste.saque(50)
teste.mostracliente()
teste.deposito(200)
teste.mostracliente()
teste.historico()

