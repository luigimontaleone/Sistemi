from BlockingQueue import BlockingQueue
from threading import RLock
class BlockingQueuePool:
    def __init__(self, n : int):
        self.code = [BlockingQueue(50) for _ in range(n)]
        self.massimo = n
        self.currentPut = 0
        self.currentTake = 0
        self.lock = RLock()
    def put(self, t):
        self.code[self.currentPut].put(t)
    def take(self):
        return self.code[self.currentTake].take()
    def nextPut(self):
        with self.lock:
            self.currentPut = (self.currentPut + 1) % self.massimo
    def nextTake(self):
        with self.lock:
            self.currentTake = (self.currentTake + 1) % self.massimo
    def getCurrentPut(self):
        with self.lock:
            return self.currentPut
    def getCurrentTake(self):
        with self.lock:
            return self.currentTake