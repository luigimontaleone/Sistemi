from BlockingQueuePool import BlockingQueuePool
from Operatore import Operatore
from Designatore import Designatore
if __name__ == '__main__':
    bq = BlockingQueuePool(5)
    op = [Operatore(bq) for _ in range(10)]
    ds = Designatore(bq)
    
    for o in op:
        o.start()
    ds.start()