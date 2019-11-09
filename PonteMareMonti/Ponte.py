from threading import RLock, Condition
class Ponte:
    def __init__(self):
        self.occupatoMareMontagna = False
        self.occupatoMontagnaMare = False
        self.lock = RLock()
        self.conditionMareMontagna = Condition(self.lock)
        self.conditionMontagnaMare = Condition(self.lock)
        self.numAttesaMareMontagna = 0
        self.numAttesaMontagnaMare = 0
    def attraversaMareMontagna(self):
        with self.lock:
            self.numAttesaMareMontagna += 1
            while self.occupatoMontagnaMare or self.numAttesaMontagnaMare > 3:
                self.conditionMareMontagna.wait()
            self.occupatoMareMontagna = True
    def attraversaMontagnaMare(self):
        with self.lock:
            self.numAttesaMontagnaMare += 1
            while self.occupatoMareMontagna or self.numAttesaMareMontagna > 3:
                self.conditionMontagnaMare.wait()
            self.occupatoMontagnaMare = True
    def attraversatoMareMontagna(self):
        with self.lock:
            self.occupatoMareMontagna = False
            self.numAttesaMareMontagna -= 1
            self.conditionMontagnaMare.notifyAll()
    def attraversatoMontagnaMare(self):
        with self.lock:
            self.numAttesaMontagnaMare -= 1
            self.occupatoMontagnaMare = False
            self.conditionMareMontagna.notifyAll()