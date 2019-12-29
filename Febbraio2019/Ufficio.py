from threading import RLock, Condition
class Ufficio:
    idUfficio = 0
    def __init__(self):
        self.id = Ufficio.idUfficio
        Ufficio.idUfficio += 1
        self.prossimoTicket = 0
        self.lock = RLock()
        self.clienti = []
        self.condition = Condition(self.lock)
    def consegnaTicket(self):
        with self.lock:
            ticket = (f"(UFFICIO:{self.id} - TICKET:{self.prossimoTicket})")
            self.clienti.append(ticket)
            self.prossimoTicket += 1
            self.condition.notifyAll()
            return ticket
    def serviCliente(self):
        with self.lock:
            while len(self.clienti) == 0:
                self.condition.wait()
            
            return self.clienti.pop(0)