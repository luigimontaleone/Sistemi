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
        #
        # Attribuisce a tutti i componenti di self.cittadini il reddito del mese corrente (780 EUR a testa), 
        # decrementando
        # soldiDisponibili e incrementando soldiErogati. Genera una eccezione e interrompe l'operazione 
        # se 
        # durante l'operazione i soldiDisponibili dovessero finire
        #
        with self.lock:
            for c in self.cittadini:
                if self.soldiDisponibili - 780 >= 0:
                    c.paga()
                    self.soldiErogati += 780
                    self.soldiDisponibili -= 780
                else:
                    print(f"Errore: soldi disponibili = {self.soldiDisponibili}")      
    def aggiungiSoldi(self, valore : int):
        #
        # incrementa self.soldiDisponibili dell'ammontare di 'valore'
        #
        with self.lock:
            self.soldiDisponibili += valore
    def iContiTornano(self):
        #
        # Verifica che la somma di quanto percepito dai singoli elementi di self.cittadini corrisponda a self.soldiErogati
        # restituisce un valore booleano in accordo
        #
        with self.lock:
            somma = 0
            for c in self.cittadini:
                somma += c.soldiPercepiti
            return somma == self.soldiErogati