from threading import RLock, Condition
class BlockingQueue:
    def __init__(self, m : int):
        self.coda = []
        self.lock = RLock()
        self.condition = Condition(self.lock)
        self.elem = m
    def put(self, t):
        with self.lock:
            while self.getFull():
                self.condition.wait()
            self.coda.append(t)
            self.condition.notifyAll()
    def take(self):
        with self.lock:
            while self.getEmpty():
                self.condition.wait()
            try:
                return self.coda.pop(0)
            finally:
                self.condition.notifyAll()
    def getFull(self):
        with self.lock:
            if len(self.coda) >= self.elem:
                return True
            return False
    def getEmpty(self):
        with self.lock:
            if len(self.coda) == 0:
                return True
            return False