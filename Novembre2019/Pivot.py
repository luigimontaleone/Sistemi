from threading import RLock, Condition
class Pivot:
    def __init__(self, n : int):
        self.criterio = True
        self.dim = n
        self.pivotQueue = []
        self.lock = RLock()
        self.condition = Condition(self.lock)
    def setCriterioPivot(self, minMax : bool):
        with self.lock:
            self.criterio = minMax
    def individuaPivot(self):
        if self.criterio == True:
            minimo = self.pivotQueue[0]
            indexMin = 0
            for i in range(0, len(self.pivotQueue)):
                if minimo < self.pivotQueue[i]:
                    minimo = self.pivotQueue[i]
                    indexMin = i
            return indexMin
        else:
            massimo = self.pivotQueue[0]
            indexMax = 0
            for i in range(0, len(self.pivotQueue)):
                if massimo > self.pivotQueue[i]:
                    massimo = self.pivotQueue[i]
                    indexMax = i
            return indexMax
    def put(self, t : int):
        with self.lock:
            if len(self.pivotQueue) == self.dim:
                self.pivotQueue.pop(self.individuaPivot())
            self.pivotQueue.append(t)
            self.condition.notifyAll()
    def take(self):
        while len(self.pivotQueue) < 2:
            self.condition.wait()
        self.pivotQueue.pop(self.individuaPivot())
        return self.pivotQueue.pop(0)