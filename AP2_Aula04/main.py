from Produto import Produto
from Perecivel import Perecivel

p1 = Produto()
p2 = Produto("Coca-Cola")
p3 = Produto("Pepsi", 5.99)

pp1 = Perecivel()
pp2 = Perecivel("Nata")
pp3 = Perecivel("Costela", 28.99)
pp4 = Perecivel( "Nhoque", 9.98, -15.3)

p3.cadastrar()
pp4.cadastrar()



