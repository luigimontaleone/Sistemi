from threading import Barrier
from Operai import Operai
import multiprocessing
class Operazione:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def sommaVettori(self):
        threadReali = multiprocessing.cpu_count()
        fetta = len(self.v1) // threadReali
        while fetta == 0:
            threadReali -= 1
            fetta = len(self.v1) // threadReali
    
        b = Barrier(threadReali + 1)
        operai = []
        for i in range(0, threadReali - 1):
            inizio = i * fetta
            fine = fetta - 1 + inizio
            operai.append(Operai(inizio, fine, self.v1, self.v2, b))
            operai[i].start()
        operai.append(Operai((threadReali - 1) * fetta, len(self.v1) - 1, self.v1, self.v2, b))
        operai[threadReali - 1].start()
        b.wait()
        
        for o in operai:
            print(f"{o.inizio}, {o.fine}, {o.getVFinale()}")