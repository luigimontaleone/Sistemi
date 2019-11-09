from Turista import Turista
from Ponte import Ponte
if __name__ == '__main__':
    ponte = Ponte(3)
    turisti = [Turista(ponte) for _ in range(8)]
    for t in turisti:
        t.start()