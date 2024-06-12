# self metodos que é ação ex: marca,modelo,numerodeplacas
#classe = automovel,cliente
#objeto = pessoa,fisca,juridica
class Carro:
    def __init__(self, marca, modelo, placa,nrodas):
        self.marca = str(marca)
        self.modelo = str(modelo)
        self.placa = str(placa)
        self.nrodas = nrodas
    def mostraCarro(self):
        print(f'Marca: {self.marca}, modelo: {self.modelo}, placa: {self.placa}, nrodas: {self.nrodas}')

teste = Carro('fiat', 'Mobi', 'RjA23-556626', 4 )
teste.mostraCarro()
teste = Carro('camaro', 'chevrolet', 'RjA23-556626', 4)
teste.mostraCarro()
