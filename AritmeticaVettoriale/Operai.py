from threading import Thread, Barrier
class Operai(Thread):
    def __init__(self, inizio : int, fine : int, v1, v2, b : Barrier):
        super().__init__()
        self.inizio = inizio
        self.fine = fine
        self.ini = self.inizio
        self.v1 = v1
        self.v2 = v2
        self.b = b
        self.vFinale = []
    def getVFinale(self):
        return self.vFinale
    def run(self):
        while self.ini <= self.fine:
            self.vFinale.append(self.v1[self.ini] + self.v2[self.ini])
            self.ini += 1
        self.b.wait()