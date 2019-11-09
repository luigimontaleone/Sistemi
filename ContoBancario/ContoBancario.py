from queue import Queue
from Transazione import Transazione
class ContoBancario:
    def __init__(self, saldo : int):
        self.saldo = saldo
        self.transazioni = Queue(50)
    