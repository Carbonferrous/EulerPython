import itertools
import numbertheory

def contfracE():
    yield 2
    n = 1
    while True:
        yield 1
        yield 2 * n
        yield 1
        n += 1

a = str(numbertheory.contfrac2real(list(itertools.islice(contfracE(), 100)))[0])
print(sum(list(map(int, (x for x in a)))))
