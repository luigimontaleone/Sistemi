from threading import Thread
from time import sleep
class Display(Thread):
    def __init__(self, sede):
        super().__init__()
        self.s = sede
    def run(self):
        while True:
            self.s.printCinque()
            sleep(0.5)