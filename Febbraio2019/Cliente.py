from threading import Thread
from Sede import Sede
class Cliente(Thread):
    def __init__(self, sede : Sede, uff):
        super().__init__()
        self.sede = sede
        self.uff = uff
    def run(self):
        while True:
            ticket = self.sede.prendiTicket(self.uff)
            print(f"Il CLIENTE {self.name} ha ricevuto il ticket {ticket}")