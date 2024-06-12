#exercicio 2 para criar

#class esses para representar estados e cidades. Cada estado tem um nome, sigla e cidades. Cada
#cidade tem nome e população. Escreva um programa de testes que crie três estados com algumas
#cidades em cada um. Exiba a população de cada estado como a soma da população de suas
#cidades.

class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
    def adiciona_cidade(self, cidade):
        cidade.estado = self
        self.cidades.append(cidade)
    def populacao(self):
        return sum([c.populacao for c in self.cidades])
class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
        self.estado = None
    def __str__(self):
        return f"Cidade (nome={self.nome}, populacao={self.populacao}, estado={self.estado})"

am = Estado("Amazonas", "AM")
am.adiciona_cidade(Cidade("Manaus", 180))
am.adiciona_cidade(Cidade("Parintins", 80))
am.adiciona_cidade(Cidade("Itacoatiara", 60))
sp = Estado("São Paulo", "SP")
sp.adiciona_cidade(Cidade("São Paulo", 500))
sp.adiciona_cidade(Cidade("Guarulhos", 200))
sp.adiciona_cidade(Cidade("Campinas", 300))
rj = Estado("Rio de Janeiro", "RJ")
rj.adiciona_cidade(Cidade("Rio de Janeiro", 400))
rj.adiciona_cidade(Cidade("São Gonçalo", 200))
rj.adiciona_cidade(Cidade("Duque de Caixias", 100))
mg = Estado("Minas Gerais", "MG")
mg.adiciona_cidade(Cidade("Belo Horizonte", 230))
mg.adiciona_cidade(Cidade("Juiz de fora", 240))
mg.adiciona_cidade(Cidade("Uberlândia", 130))

for estado in [am, sp, rj, mg]:
    print(f"Estado: {estado.nome} Sigla: {estado.sigla}")
    for cidade in estado.cidades:
        print(f"Cidade: {cidade.nome} População: {cidade.populacao}")
        print(f"População do Estado: {estado.populacao()}\n")
