class BlockingQueue:

    def __init__(self,dim):
        self.ins = 0
        self.out = 0
        self.slotPieni = 0
        self.dim = dim
        self.thebuffer = [None] * dim
        
    def put(self,c):
        self.thebuffer[self.ins] = c
        self.ins = (self.ins + 1) % len(self.thebuffer)
    def get(self):
        returnValue = self.thebuffer[self.out]
        self.out = (self.out + 1) % len(self.thebuffer)
        return returnValue