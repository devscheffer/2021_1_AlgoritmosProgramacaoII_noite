from Produto import Produto

class Perecivel(Produto):
    
    def __init__(self, nomePP = None, precoPP = 0.0, temperatura = None):
        Produto.__init__(self, nomePP, precoPP)
        self.temperatura = temperatura

    def cadastrar(self):
        print( "O produto ", self.nome, ", de preço ", self.preco,    ", de temperatura máxima ", self.temperatura, " foi cadastrado.")
