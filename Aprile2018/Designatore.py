from threading import Thread
from BlockingQueuePool import BlockingQueuePool
from random import randint
from time import sleep
class Designatore(Thread):
    def __init__(self, bq : BlockingQueuePool):
        super().__init__()
        self.bq = bq
    def run(self):
        while True:
            scelta = randint(0, 1)
            if scelta == 0:
                self.bq.nextPut()
                print(f"IL DESIGNATORE HA MANDATO AVANTI LA PUT")
            else:
                self.bq.nextTake()
                print(f"IL DESIGNATORE HA MANDATO AVANTI LA TAKE")
            
            sleep(1)
            