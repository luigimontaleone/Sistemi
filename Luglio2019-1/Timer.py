from threading import Thread
from time import sleep
class Timer(Thread):
    def __init__(self, e, timeout, tbq):
        super().__init__()
        self.timeout = timeout
        self.e = e
        self.tbq = tbq
    def run(self):
        sleep(self.timeout)
        self.tbq.getElemento(self.e, "scaduto")