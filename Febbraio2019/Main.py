from Sede import Sede
from Cliente import Cliente
from Addetto import Addetto
from Display import Display
from random import randint
if __name__ == '__main__':
    s = Sede(4)
    addetto1 = Addetto(s, 0)
    addetto2 = Addetto(s, 1)
    addetto3 = Addetto(s, 2)
    addetto4 = Addetto(s, 3)
    clienti = [Cliente(s, randint(0,3)) for _ in range(4)]
    for c in clienti:
        c.start()
    addetto1.start()
    addetto2.start()
    addetto3.start()
    addetto4.start()
    d = Display(s)
    d.start()
    