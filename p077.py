class partition:
    def __init__(self):
        self.lookupA = {2:1}
        self.lookupB = {2:1}
        self.lookupC = {2:1}
    def p(self, n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n not in self.lookup:
            self.lookup[n] = self.pa(n)
        return self.lookup[n]
    def pa(self, n):
        return n

def c(n):
    
