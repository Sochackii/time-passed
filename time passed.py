import time
class KC():
    def __init__(self):
        self.czas = time.clock()
    def dlugosc(self):
        self.czas2= time.clock()
        print(self.czas2-self.czas)
        self.czas = self.czas2
