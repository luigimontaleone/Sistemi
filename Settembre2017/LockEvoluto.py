from threading import RLock, Condition
class LockEvoluto:
    def __init__(self):
        self.lock = RLock()
        self.key = ""
    def lock(self, key):
        self.lock.acquire()
        self.key = key
    def unlock(self, key):
        if key == self.key:
            self.lock.release()
        else:
            pass
            #eccezione
    def newStepCondition(self):
        sc = StepCondition(self)
        return sc
class StepCondition:
    def __init__(self, lock):
        self.condition = lock.newStepCondition()
        self.volte = 0
        self.volteRicevute = 0
    def await_(self, volte):
        self.volte = volte
        while self.volteRicevute < self.volte:
            self.condition.wait()
        self.volteRicevute = 0
    def signal(self, volte):
        self.condition.notifyAll()
        self.volteRicevute += 1