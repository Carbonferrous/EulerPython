import numbertheory


def powpfact(n, p):
    s = 0
    while not n == 0:
        s += n//p
        n = n//p
    return s


def factfact(n):
    for p in numbertheory.primeList(n):
        yield p, powpfact(n, p)
    return

for n in range(2, 30):
    print(list(factfact(n)))
