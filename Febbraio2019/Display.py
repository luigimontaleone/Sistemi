from threading import Thread, RLock
from os.path import os
from time import sleep
class Display(Thread):
    def __init__(self, sede):
        super().__init__()
        self.s = sede
    def run(self):
        self.s.printCinque()