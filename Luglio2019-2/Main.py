from CLock import CLock
if __name__ == '__main__':
    c = CLock(3)
    print(c.getPermessi())
    c.limita(5)
    print(c.getPermessi())
    c.release()
    print(c.getPermessi())
    c.release()
    print(c.getPermessi())
    c.release()
    print(c.getPermessi())
    c.acquire()
    print(c.getPermessi())
