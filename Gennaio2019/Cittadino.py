class Cittadino():
    def __init__(self):
        self.soldiPercepiti = 0
        self.offerteRicevute = list()
        self.disoccupato = True
        
    def offriLavoro(self, nomeLavoro : str):
        #
        # Offre un lavoro a Self. Registra l'offerta nomeLavoro 
        # in self.offerteRicevute, ma solo se disoccupato = True
        #
        if self.disoccupato == True:
            self.offerteRicevute.append(nomeLavoro)
        
    def accettaLavoro(self, nomeLavoro : str):
        #
        # se nomeLavoro appartiene a self.offerteRicevute, pone self.disoccupato = False
        #
        if nomeLavoro in self.offerteRicevute:
            self.disoccupato = False
        
    def paga(self):
        #
        # Eroga 780 EUR a self, ma solo 
        # se quest'ultimo è disoccupato e il numero di offerte ricevute non supera 3
        # incrementa soldiPercepiti in accordo
        #
        if self.disoccupato == True and len(self.offerteRicevute) <= 3:
            self.soldiPercepiti += 780
        
    def getPercepito(self):
        #
        # Restituisce quanto percepito finora
        #
        return self.soldiPercepiti