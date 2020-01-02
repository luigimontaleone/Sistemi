from threading import Thread
from Pizzeria import Pizzeria
from time import sleep
class Pizzaiolo(Thread):
    def __init__(self, pizzeria : Pizzeria):
        super().__init__()
        self.pizzeria = pizzeria
    def run(self):
        while True:
            ordine = self.pizzeria.getOrdine()
            print(f"Il pizzaiolo {self.getName()} sta preparando l'ordine {ordine}")
            quantita = ordine[1]
            sleep(1 * quantita)
            print(f"Il pizzaiolo {self.getName()} sta depositando l'ordine {ordine}")
            self.pizzeria.putPizze(ordine)
            print(f"Il pizzaiolo {self.getName()} ha depositato l'ordine {ordine}")