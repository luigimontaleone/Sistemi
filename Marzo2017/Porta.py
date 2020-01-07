from BlockingQueue import BlockingQueue
from threading import Condition, RLock
class Porta:
    def __init__(self, dim):
        self.dim = dim
        self.lock = RLock()
        self.fullInputCondition = Condition(self.lock)
        self.emptyOutputCondition = Condition(self.lock)
        self.input = BlockingQueue(dim)
        self.output = BlockingQueue(dim)
    def put(self, f):
        with self.lock:
            while len(self.input) == self.dim:
                self.fullInputCondition.wait()
                
            self.emptyOutputCondition.notify_all()
            self.input.put(f)
    def get(self):
        with self.lock:
            while len(self.output) == 0:
                self.emptyOutputCondition.wait()
            
            self.fullInputCondition.notify_all()
            self.input.get()