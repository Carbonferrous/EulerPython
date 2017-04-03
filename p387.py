import numbertheory


def dsum(n):
    return sum(map(int, (i for i in str(n))))

Hnum = list(i for i in range(1, 10))
Hnumi = list(i for i in Hnum)
Hnumj = []
SHnum = []
total = 0
for l in range(12):
    for h in Hnumi:
        for i in range(10):
            n = 10*h + i
            d = dsum(n)
            if n % d == 0:
                Hnumj += [n]
                if numbertheory.isPrime(n // d):
                    SHnum += [n]
    Hnum += list(i for i in Hnumj)
    Hnumi = list(i for i in Hnumj)
    Hnumj = []
for s in SHnum:
    for i in [1, 3, 7, 9]:
        n = 10*s+i
        if numbertheory.isPrime(n):
            total += n
print(total)