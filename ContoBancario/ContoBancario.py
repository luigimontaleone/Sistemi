from Transazione import Transazione
from threading import RLock
class ContoBancario:
    ID = 1
    def __init__(self, s : int):
        self.saldo = s
        self.transazioni = list()
        self.id = ContoBancario.ID
        ContoBancario.ID += 1
        self.lock = RLock()
    def addTransazione(self, t : Transazione):
        if(len(self.transazioni) == 50):
            self.transazioni.pop(0)
        self.transazioni.append(t) 