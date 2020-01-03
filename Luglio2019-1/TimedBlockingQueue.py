from _collections import deque
from threading import RLock, Condition
from Timer import Timer
class TimedBlockingQueue:
    def __init__(self, dim):
        self.coda = deque()
        self.lock = RLock()
        self.dim = dim
        self.estratto = False
        self.condition = Condition(self.lock)
    def timedPut(self, e, timeout):
        with self.lock:
            while len(self.coda) == self.dim:
                self.condition.wait()
            self.coda.append(e)
            t = Timer(e, timeout, self)
            t.start()
    def waitFor(self, e):
        with self.lock:
            while e in self.coda:
                self.condition.wait()
            return self.estratto
    def getElemento(self, e, val):
        with self.lock:
            if e in self.coda:
                self.coda.remove(e)
                if val == "estratto":
                    self.estratto = True
                else:
                    self.estratto = False
            else:
                self.estratto = False
            self.condition.notifyAll()