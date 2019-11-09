from Turista import Turista
from Ponte import Ponte
if __name__ == '__main__':
    ponte = Ponte()
    turisti = [Turista(ponte) for _ in range(5)]
    for t in turisti:
        t.start()