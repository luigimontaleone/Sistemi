from threading import RLock, Condition
class CLock:
    def __init__(self, permessi : int):
        self.permessi = permessi
        self.lock = RLock()
        self.condition = Condition(self.lock)
        self.permessiMax = 0
    def acquire(self):
        with self.lock:
            while self.permessi == 0:
                self.condition.wait()
            self.permessi -= 1
    def release(self):
        with self.lock:
            if self.permessiMax != 0 and self.permessi + 1 <= self.permessiMax:
                self.permessi += 1
            self.condition.notifyAll()
    def limita(self, n : int):
        self.permessiMax = n
    def getPermessi(self):
        return self.permessi
    def getPermessiMax(self):
        return self.permessiMax