from threading import RLock, Condition
class SharedInteger():
    def __init__(self):
        self.number = 0
        self.lock = RLock()
        self.condition = Condition(self.lock)
    def get(self):
        with self.lock:
            return self.number
    def set(self, n : int):
        with self.lock:
            self.number = n
            self.condition.notifyAll()
    def inc(self, i):
        if isinstance(i, SharedInteger):
            self.lock.acquire()
            i.lock.acquire()
            self.number += i.get()
            self.condition.notifyAll()
            i.condition.notifyAll()    
            self.lock.release()
            i.lock.release()
        else:
            with self.lock:
                self.number += i
                self.condition.notifyAll()
    def waitForAtLeast(self, soglia):
        with self.lock:
            while self.number < soglia:
                self.condition.wait()
            return self.number
    def setInTheFuture(self, i, soglia, valore):
        with self.lock:
            while i.get() < soglia:
                self.condition.wait()
            self.number = valore