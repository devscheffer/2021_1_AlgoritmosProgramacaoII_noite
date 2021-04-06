from Pessoa import Pessoa

class Fisica(Pessoa):
    
    def __init__(self, cod, name, cpf):     
        Pessoa.__init__(self, cod, name)
        self.cpf = cpf
        print("CPF: ", self.cpf)
