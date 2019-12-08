from threading import Thread
from Banca import Banca
from random import randint
from ContoBancario import ContoBancario
class Cliente(Thread):
    def __init__(self, b : Banca, c1 : ContoBancario, c2 : ContoBancario):
        super().__init__()
        self.banca = b
        self.c1 = c1
        self.c2 = c2
    def run(self):
        while True:
            importo = randint(1, 10)
            print(f"il cliente {self.name} sta provando a trasferire {importo} da {self.c1.id} a {self.c2.id}")
            self.banca.trasferisci(self.c1, self.c2, importo)
            print(f"il cliente {self.name} ha trasferito {importo} da {self.c1.id} a {self.c2.id}")
            print(f"il conto {self.c1.id} ha ora {self.c1.saldo}")