from Cittadino import Cittadino
from Popolo import Popolo
if __name__ == '__main__':
    citt = [Cittadino() for _ in range(49)]
    p = Popolo()
    p.assegnaCittadini(citt)
    while True:
        p.distribuisciReddito()