import itertools
target = 4
coins = 8
print("sum: %d" % next(next((nways >> n2) + (1 << (coins - n2)) for n2 in (next(filter(lambda n: (nways >> n) & 1, itertools.count())),)) for nways in (sum(1 for _ in filter(lambda x: target in itertools.accumulate(x), itertools.product((-1, 1), repeat=coins))),)))
