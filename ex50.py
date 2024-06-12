#exercio corrigido Dontpad
class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, idade):
        if (self.idade < 21):
            self.altura += 0.02
            self.idade += idade
        if (self.idade > 60):
            self.altura -= 0.01
            self.idade += idade
        self.idade += idade

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def mostraPessoa(self):
        print(f'Nome: {self.nome}, idade: {self.idade} anos, peso: {self.peso}kg, altura: {self.altura}cm')


ana = Pessoa('Ana', 19, 54, 163)
marcos = Pessoa( 'Marcos', 6, 30, 1.23)
maria = Pessoa('Maria', 65, 56, 1.60)
ana.mostraPessoa()
ana.emagrecer(6)
ana.crescer(0.2)
ana.mostraPessoa()
ana.engordar(5)
ana.mostraPessoa()

marcos.mostraPessoa()
marcos.envelhecer(4)
marcos.emagrecer(6)
marcos.crescer(0.2)
marcos.mostraPessoa()
marcos.engordar(5)
marcos.mostraPessoa()

maria.mostraPessoa()
maria.envelhecer(4)
maria.emagrecer(6)
maria.crescer(-0.2)
maria.mostraPessoa()
maria.engordar(5)
maria.mostraPessoa()

