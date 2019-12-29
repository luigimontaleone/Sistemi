from threading import Thread, RLock
from random import randint
from Pizzeria import Pizzeria
from time import sleep
class Cliente(Thread):
    def __init__(self, pizzeria : Pizzeria):
        super().__init__()
        self.pizzeria = pizzeria
    def run(self):
        while(True):
            quantita = randint(1, 5)
            idPizza = randint(1, 10)
            ordine = (idPizza, quantita)
            self.pizzeria.putOrdine(ordine)
            print(f"Il cliente {self.getName()} ha ordinato l'ordine {ordine}")
            sleep(1 * quantita)
            print(f"Il cliente {self.getName()} sta aspettando l'ordine {ordine}")
            if self.pizzeria.getPizze(ordine):
                print(f"Il cliente {self.getName()} ha ricevuto l'ordine {ordine}")
            else:
                print("QUESTO NON DEVE MAI ESSERE STAMPATO")