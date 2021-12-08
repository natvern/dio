class Controller():
    def __init__(self, xl, vl):
        self.vehicles = len(xl) 
        self.xl = xl 
        self.vl = vl 
    
    def isSafe(self, al): 
        previous = -float("inf")
        for i in range(self.vehicles):
            v = self.vl[i] + al[i]
            if self.xl[i] + v < previous:
                return False 
            previous = self.xl[i] + v
        for i in range(self.vehicles):
            self.vl[i] = self.vl[i] + al[i]
        return True