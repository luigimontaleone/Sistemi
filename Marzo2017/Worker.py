from threading import Thread
from Switch import Switch
from random import randint
class Worker(Thread):
    def __init__(self, s : Switch):
        super().__init__()
        self.s = s
    def run(self):
        scelta = randint(0, self.s.maxDimCode - 1)
        frame = self.s.receiveFrame(scelta)