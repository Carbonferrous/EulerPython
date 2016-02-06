# infinite precision continued fraction of an irrational number
import itertools
import math
from fractions import gcd

class Irrational:
    def __init__(self, topI, topF, bottom):
        g = gcd(gcd(topI, topF), bottom)
        self.topI = topI // g
        self.topF = topF // g
        self.bottom = bottom // g
    @classmethod
    def sqrt(self, num):
        approx = int(math.sqrt(num))
        if (approx) * (approx) == num:
            return self(approx, 0, 1)
        return self(0, num, 1)
    def recip(self):
        # c/(a + \b)
        # (c(a-\b))/(a*a-b)
        # c/(a - \b)
        # (c(a+\b))/(a*a-b)
        a = self.topI
        b = self.topF
        c = self.bottom
        return Irrational(c * a, -c * b, a * a - abs(b))
    def __sub__(self, other):
        return Irrational(self.topI - other * self.bottom, self.topF, self.bottom)
    def __int__(self):
        a = self.topI
        b = self.topF
        c = self.bottom
        sgn = 1 if b > 0 else -1
        ab = abs(b)
        app = int(math.sqrt(ab))
        while app * app < ab:
            app += 1
        while app * app > ab:
            app -= 1
        return (a + app) // c

def gencont(n):
    while True:
        yield int(n)
        n = (n - int(n)).recip()

print(list(itertools.islice(gencont(Irrational.sqrt(7)), 100)))
