from threading import RLock, Condition
class DatoCondiviso():
    
    SOGLIAGIRI = 5
    
    def __init__(self, v):
        self.dato = v
        self.ceLockScrittura = False
        self.numScrittoriInAttesa = 0
        self.numLettori = 0
        self.lock = RLock()
        self.conditionRead = Condition(self.lock)
        self.conditionWrite = Condition(self.lock)
        self.numGiriSenzaScrittori = 0
    
    def getDato(self):
        return self.dato

    def setDato(self, v):
        self.dato = v
        
    def acquireReadLock(self):
        with self.lock:
            while self.ceLockScrittura or (self.numScrittoriInAttesa > 0  and \
                                           self.numGiriSenzaScrittori > self.SOGLIAGIRI) :
                self.conditionRead.wait()
            self.numLettori += 1
            self.numGiriSenzaScrittori += 1
    
    def releaseReadLock(self):
        with self.lock:
            self.numLettori -= 1
            if self.numLettori == 0:
                self.conditionWrite.notify()
    
    def acquireWriteLock(self):
        with self.lock:
            self.numScrittoriInAttesa += 1
            while self.ceLockScrittura or self.numLettori > 0:
                self.conditionWrite.wait()
            self.ceLockScrittura = True
            self.numScrittoriInAttesa -= 1
            self.numGiriSenzaScrittori = 0
    
    def releaseWriteLock(self):
        with self.lock:
            self.ceLockScrittura = False
            self.conditionWrite.notify()
            self.conditionRead.notifyAll()