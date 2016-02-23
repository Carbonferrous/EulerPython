class partition:
    def __init__(self):
        self.lookup = {0:1}
    def p(self, n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n not in self.lookup:
            self.lookup[n] = self.pa(n)
        return self.lookup[n]
    def pa(self, n):
        s = 0
        m = 1
        penta =  1
        while penta <= n:
            s += int((-1)**(m-1))*self.p(n-penta)
            if m > 0:
                m = -1 * m
            else:
                m = -1 * m + 1
            penta =  m*(3*m-1)//2
        return s

pasdf = partition()
a = 0
while pasdf.p(a) % 1000000 != 0:
    a += 1
print(a)
