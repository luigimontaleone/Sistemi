from TimedBlockingQueue import TimedBlockingQueue
from GeneralThread import GeneralThread
if __name__ == '__main__':
    tbq = TimedBlockingQueue(20)
    g1 = GeneralThread(tbq, 1)
    g2 = GeneralThread(tbq, 2)
    g1.start()
    g2.start()
    