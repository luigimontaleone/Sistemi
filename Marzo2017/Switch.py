from threading import RLock
from Porta import Porta
from Frame import Frame
class Switch:
    def __init__(self, nPorte, maxDimCode):
        self.maxDimCode = maxDimCode
        self.nPorte = nPorte
        self.lock = RLock()
        self.porte = [Porta(self.maxDimCode) for _ in range(self.nPorte)]
        
    def sendFrame(self, f : Frame, p : int):
        with self.lock:
            self.porte[p].put(f)
    def receiveFrame(self, p : int):
        with self.lock:
            self.porte[p].get()