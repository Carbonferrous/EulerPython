class memorize:
    def __init__(self):
        #initialize base case
        self.lookup = {1:1, 3:3}
    def function(self, n):
        #write function with self.get() for recursive calls
        if n & 1 == 0:
            return self.get(n >> 1)
        if n & 3 == 1:
            return (self.get((n >> 1) + 1) << 1) - self.get(n >> 2)
        else:
            return self.get(((n >> 2) << 1) + 1) * 3 - (self.get(n >> 2) << 1)
    def get(self, n):
        if n not in self.lookup:
            self.lookup[n] = self.function(n)
        return self.lookup[n]


f = memorize()
