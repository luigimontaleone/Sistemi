class Cittadino():
    def __init__(self):
        self.soldiPercepiti = 0
        self.offerteRicevute = list()
        self.disoccupato = True
        
    def offriLavoro(self, nomeLavoro : str):
        if self.disoccupato == True:
            self.offerteRicevute.append(nomeLavoro)
        
    def accettaLavoro(self, nomeLavoro : str):
        if nomeLavoro in self.offerteRicevute:
            self.disoccupato = False
        
    def paga(self):
        if self.disoccupato == True and len(self.offerteRicevute) <= 3:
            self.soldiPercepiti += 780
        
    def getPercepito(self):
        return self.soldiPercepiti