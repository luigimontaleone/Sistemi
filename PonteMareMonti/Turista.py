from threading import Thread
from Ponte import Ponte
from random import randint, random
from time import sleep
class Turista(Thread):
    def __init__(self, p : Ponte):
        super().__init__()
        self.ponte = p
    def run(self):
        while True:
            direzione = randint(0, 2)
            if direzione == 0:
                print(f"il turista {self.name} vuole andare dal mare alla montagna")
                self.ponte.attraversaMareMontagna()
                sleep(random())
                print(f"il turista {self.name} ha attraversato dal mare alla montagna")
                self.ponte.attraversatoMareMontagna()
            elif direzione == 1:
                print(f"il turista {self.name} vuole andare dalla montagna al mare")
                self.ponte.attraversaMontagnaMare()
                sleep(random())
                print(f"il turista {self.name} ha attraversato dalla montagna al mare")
                self.ponte.attraversatoMontagnaMare()