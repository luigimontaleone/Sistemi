from threading import Thread
from Ponte import Ponte
from random import randint, random
from time import sleep
class Turista(Thread):
    def __init__(self, p : Ponte):
        super().__init__()
        self.ponte = p
    def run(self):
        #while True:
        direzione = 0#randint(0, 2)
        if direzione == 0:
            print(f"{self.name} VUOLE ANDARE dal mare alla montagna")
            self.ponte.attraversaMareMontagna(self.name)
            print(f"{self.name} STA ATTRAVERSANDO dal mare alla montagna")
            sleep(random())
            self.ponte.attraversatoMareMontagna(self.name)
            print(f"{self.name} HA ATTRAVERSATO dal mare alla montagna")
        elif direzione == 1:
            print(f"{self.name} VUOLE ANDARE dalla montagna al mare")
            self.ponte.attraversaMontagnaMare(self.name)
            sleep(random())
            self.ponte.attraversatoMontagnaMare(self.name)
            print(f"{self.name} HA ATTRAVERSATO dalla montagna al mare")