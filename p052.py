import itertools
n = 1
while True:
    i = list(map(int, [''.join(a) for a in itertools.permutations(str(n))]))
    if all(n * k in i for k in range(1, 7)):
        break
    n += 1
print(n)
