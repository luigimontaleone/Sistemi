from Ufficio import Ufficio
from threading import RLock, Condition
from os.path import os
from time import sleep
class Sede:
    def __init__(self, n : int):
        self.uffici = [Ufficio() for _ in range(n)]
        self.lock = RLock()
        self.condition = Condition(self.lock)
        self.ticketServiti = []
    def prendiTicket(self, uff):
        t = self.uffici[uff].consegnaTicket()
        return t
    def chiamaTicket(self, uff):
        self.ticketServiti.append(self.uffici[uff].serviCliente())
        with self.lock:
            self.condition.notifyAll()
            if len(self.ticketServiti) + 1 > 5:
                self.ticketServiti.pop(0)
    def waitForTicket(self, ticket):
        while ticket not in self.ticketServiti:
            self.condition.wait()
    def printAttese(self):
        with self.lock:
            # os.system('cls')
            for u in self.uffici:
                print(f"{u.id}: {len(u.clienti)}\n")
            sleep(2)
    def printCinque(self):
        with self.lock:
            print(f"{self.ticketServiti}\n")
            sleep(1)