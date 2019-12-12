from threading import Thread
from Sede import Sede
class Addetto(Thread):
    def __init__(self, sede : Sede, uff):
        super().__init__()
        self.sede = sede
        self.uff = uff
    def run(self):
        while True:
            self.sede.chiamaTicket(self.uff)
            