from threading import RLock, Condition
from queue import Queue
class Ponte:
    def __init__(self, n : int):
        self.occupatoMareMontagna = False
        self.occupatoMontagnaMare = False
        self.lock = RLock()
        self.conditionMareMontagna = Condition(self.lock)
        self.conditionMontagnaMare = Condition(self.lock)
        self.numAttesaMareMontagna = 0
        self.numAttesaMontagnaMare = 0
        self.queueAuto = list()
        self.queueEntrataMare = list()
        self.queueEntrataMontagna = list()
        self.numMax = n
    def attraversaMareMontagna(self, name):
        with self.lock:
            self.queueEntrataMare.append(name)
            self.numAttesaMareMontagna += 1
            while self.occupatoMontagnaMare or self.numAttesaMontagnaMare > 3 or len(self.queueAuto) == self.numMax or self.queueEntrataMare[0] != name:
                self.conditionMareMontagna.wait()
            self.queueEntrataMare.pop(0)
            self.queueAuto.append(name)
            print(self.queueAuto)
            self.occupatoMareMontagna = True
    def attraversaMontagnaMare(self, name):
        with self.lock:
            self.queueEntrataMontagna = list()
            self.numAttesaMontagnaMare += 1
            while self.occupatoMareMontagna or self.numAttesaMareMontagna > 3 or len(self.queueAuto) == self.numMax or self.queueEntrataMontagna[0] != name:
                self.conditionMontagnaMare.wait()
            self.queueEntrataMontagna.pop(0)
            self.queueAuto.append(name)
            print(self.queueAuto)
            self.occupatoMontagnaMare = True
    def attraversatoMareMontagna(self, name):
        with self.lock:
            while self.queueAuto[0] != name or len(self.queueAuto) == 0:
                self.conditionMareMontagna.wait()
            self.queueAuto.pop(0)
            self.occupatoMareMontagna = False
            self.numAttesaMareMontagna -= 1
            self.conditionMareMontagna.notifyAll()
            self.conditionMontagnaMare.notifyAll()
    def attraversatoMontagnaMare(self, name):
        with self.lock:
            while self.queueAuto[0] != name or len(self.queueAuto) == 0:
                self.conditionMontagnaMare.wait()
            self.queueAuto.pop(0)
            self.numAttesaMontagnaMare -= 1
            self.occupatoMontagnaMare = False
            self.conditionMareMontagna.notifyAll()
            self.conditionMontagnaMare.notifyAll()