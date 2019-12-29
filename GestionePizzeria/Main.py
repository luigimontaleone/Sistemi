from Cliente import Cliente
from Pizzaiolo import Pizzaiolo
from threading import Thread
from Pizzeria import Pizzeria
def main():
    clienti = [Cliente] * 5
    pizzaioli = [Pizzaiolo] * 2
    pizzeria = Pizzeria(10, 10)
    for c in clienti:
        c = Cliente(pizzeria)
        c.start()
    for p in pizzaioli:
        p = Pizzaiolo(pizzeria)
        p.start()
if __name__ == '__main__':
    main()