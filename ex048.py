class Cao:
    def __init__(self, nome, ccor, corolhos, altura, peso):
        self.nome = str(nome)
        self.ccor = str(ccor)
        self.corolhos = str(corolhos)
        self.altura = altura
        self.peso = peso

    def latir(self):
        print('Au - Au')
    def mostrarCao(self):
        print(f'nome: {self.nome}, cor: {self.ccor}, cor dos olhos: {self.corolhos}, altura: {self.altura}, peso {self.peso}')


cachorro1 = Cao('Bolt', 'Castanho', 'Preto', 90, 15)
cachorro1.mostrarCao()

cachorro1.latir()
