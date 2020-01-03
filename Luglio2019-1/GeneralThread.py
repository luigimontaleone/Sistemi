from threading import Thread
from random import randint
from time import sleep
class GeneralThread(Thread):
    def __init__(self, tbq, tipo):
        super().__init__()
        self.tbq = tbq
        self.tipo = tipo
    def run(self):
        e = 3
        if self.tipo == 1:
            self.tbq.timedPut(e, 1.5)
            print(f"{self.name}:    elemento inserito correttamente")
            if self.tbq.waitFor(e):
                print(f"{self.name}:    ELEMENTO ESTRATTO CORRETTAMENTE")
            else:
                print(f"{self.name}:    ELEMENTO SCADUTO")
        else:
            sleep(randint(1, 2))
            self.tbq.getElemento(e, "estratto")