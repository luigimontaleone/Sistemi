from queue import Queue
from threading import Condition, RLock

class Pizzeria():
    def __init__(self, dimOrdini, dimPizze):
        self.ordini = Queue(dimOrdini)
        self.pizzePronte = []
        self.lock = RLock()
        self.condition = Condition(self.lock)
        self.dimPizze = dimPizze
    def putOrdine(self, ordine):
        self.ordini.put(ordine)
    def getOrdine(self):
        return self.ordini.get() #True da aggiungere
    def putPizze(self, ordine):
        with self.lock:
            while len(self.pizzePronte) == self.dimPizze:
                self.condition.wait()
            self.pizzePronte.append(ordine)
            self.condition.notifyAll()
    def getPizze(self, ordine):
        with self.lock:
            while not ordine in self.pizzePronte:
                self.condition.wait()
            for o in self.pizzePronte:
                if o == ordine:
                    self.pizzePronte.remove(ordine)
                    self.condition.notifyAll()
                    return True
        return False
    