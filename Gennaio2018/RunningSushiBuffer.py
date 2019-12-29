from threading import RLock, Condition
class RunningSushiBuffer:
    def __init__(self, n : int):
        self.lock = RLock()
        self.condition = Condition(self.lock)
        self.buffer = [0] * n
        self.slot = n
    def put(self, t):
        with self.lock:
            while self.buffer[0]:
                self.condition.wait()
            self.buffer[0] = t
    def get(self, i : int):
        if i < 1 or i > self.slot - 1:
            print(f"error")
            return False
        with self.lock:
            while not self.buffer[i]:
                self.condition.wait()
            elem = self.buffer[i]
            self.buffer[i] = 0
            return elem
    def shift(self, j : int = 1):
        if j < 1 or len(self.buffer) <= 1:
            return False
        with self.lock:
            while j > 0:
                i = len(self.buffer) - 1
                temp = self.buffer[0]
                while i > 0:
                    self.buffer[(i + 1) % len(self.buffer)] = self.buffer[i]
                    i -= 1
                self.buffer[1] = temp
                j -= 1
	        self.condition.notifyAll()