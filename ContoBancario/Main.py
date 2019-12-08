from Banca import Banca
from ContoBancario import ContoBancario
from Cliente import Cliente
if __name__ == '__main__':
    c1 = ContoBancario(100)
    c2 = ContoBancario(200)
    b = Banca([c1, c2])
    cliente1 = Cliente(b, c1, c2)
    cliente2 = Cliente(b, c2, c1)
    cliente1.start()
    cliente2.start()