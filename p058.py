from numbertheory import isPrime
class Spiral:
    def __init__(self):
        self.side = 1
        self.index = 1
        self.diag = self.getdiagonal()
    def __next__(self):
        return next(self.diag)
    def getdiagonal(self):
        yield self.index
        self.side += 2
        while True:
            for s in range(4):
                self.index += self.side - 1
                yield self.index
            self.side += 2


x = Spiral()
primediag = 0
totaldiag = 1
next(x)
while True:
    diag = next(x)
    if isPrime(diag):
        primediag += 1
    totaldiag += 1
    if primediag/totaldiag < .1:
        break
print(x.side)
