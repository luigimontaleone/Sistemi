from ContoBancario import ContoBancario
class Transazione:
    def __init__(self, s : ContoBancario, d : ContoBancario, importo : int):
        self.sorgente = d
        self.destinazione = d
        self.importo = importo
        