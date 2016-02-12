import itertools
def contfrac2():
    n = 2
    d = 1
    while True:
        n, d = d, n
        n = 2 * d + n
        yield [d + n, n]
count = 0
n = list(itertools.islice(contfrac2(), 1000))
for x in range(1, 1000):
    if len(str(n[x][0])) > len(str(n[x][1])):
        count += 1
print(count)
