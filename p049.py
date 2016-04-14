import numbertheory
import itertools
plist = [x for x in numbertheory.primeList(10000)]
for x in plist:
    i = list(map(int, [''.join(a) for a in itertools.permutations(str(x))]))
    for y in plist:
        if x < y and y != x and y in i and y in plist and (2 * y - x) in i and (2 * y - x) in plist:
            print(x, y, (2 * y - x))
