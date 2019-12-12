from threading import RLock
from queue import Queue
class Ufficio:
    idUfficio = 'A'
    def __init__(self):
        self.id = Ufficio.idUfficio
        Ufficio.idUfficio += 1
        self.prossimoTicket = 0
        
        self.clienti = Queue()
        self.lock = RLock()
    def consegnaTicket(self):
        with self.lock:
            ticket = (f"{self.id}{self.prossimoTicket}")
            self.clienti.put(ticket)
            return self.ticket
    def serviCliente(self):
        with self.lock:
            return self.clienti.get()