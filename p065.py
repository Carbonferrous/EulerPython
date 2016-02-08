import itertools
def contfracE():
    yield 2
    n = 1
    while True:
        yield 1
        yield 2 * n
        yield 1
        n += 1
def contfrac2real(a):
    n = a[len(a) - 1]
    d = 1
    for i in range(len(a) - 2, -1, -1):
        n, d = d, n
        n = a[i] * d + n
    return [n, d]
print(str(contfrac2real(list(itertools.islice(contfracE(), 100)))[0]))
