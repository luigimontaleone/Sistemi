from threading import RLock
class Popolo:         
    def __init__ (self):
        self.soldiErogati = 0
        self.soldiDisponibili = 1000000000
        self.cittadini = list()
        self.lock = RLock()
    def assegnaCittadini(self, cittadiniList):
        self.cittadini = cittadiniList
    def distribuisciReddito(self):
        with self.lock:
            for c in self.cittadini:
                if self.soldiDisponibili - 780 >= 0:
                    c.paga()
                    self.soldiErogati += 780
                    self.soldiDisponibili -= 780
                else:
                    print(f"Errore: soldi disponibili = {self.soldiDisponibili}")      
    def aggiungiSoldi(self, valore : int):
        with self.lock:
            self.soldiDisponibili += valore
    def iContiTornano(self):
        with self.lock:
            somma = 0
            for c in self.cittadini:
                somma += c.soldiPercepiti
            return somma == self.soldiErogati