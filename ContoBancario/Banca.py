from ContoBancario import ContoBancario
from Transazione import Transazione
class Banca:
    def __init__(self, c : []):
        self.conti = c;
    def getSaldo(self, c : ContoBancario):
        index = self.conti.index(c)
        return self.conti[index].saldo
    def trasferisci(self, sorgente : ContoBancario, destinazione : ContoBancario, importo : int):
        try:
            if sorgente.id < destinazione.id:
                sorgente.lock.acquire()
                destinazione.lock.acquire()
            else:
                destinazione.lock.acquire()
                sorgente.lock.acquire()
            if sorgente.saldo < importo:
                return False
            destinazione.saldo += importo
            sorgente.saldo -= importo
            t = Transazione(sorgente, destinazione, importo)
            sorgente.addTransazione(t)
            destinazione.addTransazione(t)
        finally:
            sorgente.lock.release()
            destinazione.lock.release()
        return True