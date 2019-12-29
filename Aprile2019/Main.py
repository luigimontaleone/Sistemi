from Candidato import Candidato
from Elezione import Elezione
from Elettore import Elettore
if __name__ == '__main__':
    candidati = []
    c1 = Candidato("Marcello")
    candidati.append(c1)
    c2 = Candidato("Mario")
    candidati.append(c2)
    c3 = Candidato("Proto")
    candidati.append(c3)
    c4 = Candidato("Ugo")
    candidati.append(c4)
    numEl = 4
    e = Elezione(candidati, numEl)
    e.apriElezione()
    elettori = [Elettore(e) for _ in range(15)]
    for el in elettori:
        el.start()
    res = e.waitForRisultati()
    for c in res:
        c.stampa()