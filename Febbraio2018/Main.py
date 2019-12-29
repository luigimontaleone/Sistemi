from Operatore import Operatore
from SharedInteger import SharedInteger

if __name__ == '__main__':
    sharedInt1 = SharedInteger()
    sharedInt2 = SharedInteger()
    op = [Operatore(sharedInt1, sharedInt2) for _ in range(6)]
    for o in op:
        o.start()