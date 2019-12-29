from threading import RLock, Condition
from Candidato import Candidato
class Elezione:
    def __init__(self, candidati : [], elettori : int):
        self.candidati = candidati
        self.numElettori = elettori
        self.elezioneAperta = False
        self.maiAperta = True
        self.lock = RLock()
        self.condition = Condition(self.lock)
    def apriElezione(self):
        with self.lock:
            self.elezioneAperta = True
    def chiudiElezione(self):
        with self.lock:
            self.elezioneAperta = False
            self.condition.notifyAll()
    def vota(self, c : Candidato):
        with self.lock:
            if self.getVoti() + 1 > self.numElettori:
                self.chiudiElezione()
                return False
            index = -1
            index = self.candidati.index(c)
            if index == -1:
                return False
            self.candidati[index].votiAcquisiti += 1
    def getVoti(self):
        with self.lock:
            voti = 0
            for c in self.candidati:
                voti += c.votiAcquisiti
            return voti
    def waitForRisultati(self):
        with self.lock:
            while self.elezioneAperta:
                self.condition.wait()
            self.ordinaPerVoti()
            return self.candidati
    def ordinaPerVoti(self):
        for i in range(0, len(self.candidati) - 1):
            for j in range(i + 1, len(self.candidati)):
                if self.candidati[i].votiAcquisiti < self.candidati[j].votiAcquisiti:
                    cTemp = self.candidati[i]
                    self.candidati[i] = self.candidati[j]
                    self.candidati[j] = cTemp
    def getDisp(self):
        with self.lock:
            if self.elezioneAperta:
                return True
            return False