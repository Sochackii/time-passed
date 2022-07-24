import time

class KC:
    
    def __init__(self):
        self.Time = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
        
    def TimePassed(self):
        self.Time2= time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
        print(self.Time2-self.Time)
        self.Time = self.Time2
