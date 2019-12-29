class Candidato:
    def __init__(self, nome):
        self.nome = nome
        self.votiAcquisiti = 0
    def stampa(self):
        print(f"{self.nome}: {self.votiAcquisiti}\n")