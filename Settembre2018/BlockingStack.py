from threading import RLock, Condition
class BlockingStack:
    def __init__(self, dim):
        self.dim = dim
        self.blockingStack = []
        self.lock = RLock()
        self.condition = Condition(self.lock)
    def put(self, t):
        with self.lock:
            while len(self.blockingStack >= self.dim):
                self.condition.wait()
            self.blockingStack.append(t)
            self.condition.notifyAll()
    def take(self, t = self.dim - 1):
        self.lock.acquire()
        while t not in self.blockingStack:
            self.condition.wait()
        try:
            return self.blockingStack.pop(self.blockingStack.index(t))
        finally:
            self.condition.notifyAll()
            self.lock.release()
            
    