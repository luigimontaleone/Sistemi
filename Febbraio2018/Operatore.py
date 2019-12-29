from threading import Thread
from SharedInteger import SharedInteger
from time import sleep
class Operatore(Thread):
    def __init__(self, s1 : SharedInteger, s2 : SharedInteger):
        super().__init__()
        self.s1 = s1
        self.s2 = s2
    def run(self):
        while True:
            self.s2.inc(1)
            print(f"{self.name} Valore attuale di s2: {self.s2.get()}")
            self.s1.inc(self.s2)
            print(f"{self.name} Valore attuale di s1: {self.s1.get()}")
            sleep(0.5)