from Ufficio import Ufficio
from threading import RLock, Condition
from os.path import os
from time import sleep
class Sede:
    def __init__(self, n : int):
        self.uffici = [Ufficio for _ in range(n)]
        self.lock = RLock()
        self.condition = Condition(self.lock)
        self.ticketServiti = []
    def prendiTicket(self, uff):
        return self.uffici[uff].consegnaTicket()
    def chiamaTicket(self, uff):
        if len(self.ticketServiti) >= 5:
            self.ticketServiti.pop(0)
        self.ticketServiti.append(self.uffici[uff].serviCliente())
        self.condition.notifyAll()
    def waitForTicket(self, ticket):
        while ticket not in self.ticketServiti:
            self.condition.wait()
        return
    def printAttese(self):
        with self.lock:
            # os.system('cls')
            for u in self.uffici:
                print(f"{u.id}: {len(u.clienti)}\n")
            sleep(2)
    def printCinque(self):
        with self.lock:
            print(f"{self.s.ticketServiti}\n")
            sleep(1)