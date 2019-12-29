from threading import Thread
from Elezione import Elezione
from random import randint
class Elettore(Thread):
    def __init__(self, e : Elezione):
        super().__init__()
        self.e = e
    def run(self):
        if self.e.getDisp():
            indexCandidato = randint(0, len(self.e.candidati) - 1)
            c = self.e.candidati[indexCandidato]
            print(f"{self.name} VUOLE votare {c.nome}...")
            self.e.vota(c)
            print(f"{self.name} HA votato {c.nome}...")