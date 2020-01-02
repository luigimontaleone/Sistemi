from threading import Thread
from BlockingQueuePool import BlockingQueuePool
from random import randint
from time import sleep
class Operatore(Thread):
    def __init__(self, bq : BlockingQueuePool):
        super().__init__()
        self.bq = bq
    def run(self):
        while True:
            scelta = randint(0, 10)
            if scelta <= 7:
                num = randint(0, 10)
                print(f"{self.name} sta cercando di inserire {num} nella coda {self.bq.getCurrentPut()}")
                self.bq.put(num)
                print(f"{self.name} HA INSERITO {num} nella coda {self.bq.getCurrentPut()}")
            else:
                print(f"{self.name} sta cercando di prelevare dalla coda {self.bq.getCurrentPut()}")
                num = self.bq.take()
                print(f"{self.name} HA PRELEVATO {num} dalla coda {self.bq.getCurrentTake()}")
            
            sleep(2)