class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = str(nome)
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)

    def mostrarpessoa(self):
        print(f'nome, {self.nome},idade {self.idade},peso {self.peso},altura {self.altura}')
    def envelhecer(self):
        print(self.idade+5)
    def engordar(self):
         print(self.peso+7)
    def emagrecer(self):
        print(self.peso-10)
    def crescer(self):
        print(self.altura+1)

pessoa1 = Pessoa('robert', 21, 80, 172)
pessoa1.mostrarpessoa()
pessoa1.envelhecer()
pessoa1.engordar()
pessoa1.emagrecer()
pessoa1.crescer()