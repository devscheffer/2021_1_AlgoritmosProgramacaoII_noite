from Conta import Conta

c1 = Conta()
c1.imprimirSaldo()

c1.depositar( 10.5 )
c1.imprimirSaldo()

c1.sacar( 5.2 )
c1.imprimirSaldo()

c1.__saldo = 20
c1.imprimirSaldo()
