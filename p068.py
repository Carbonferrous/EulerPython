import itertools
def magicNgon(l):
    if len(l) & 1 == 1:
        return 0
    sums = [(l[x] + l[x+1] + l[(x+3) % len(l)]) for x in range(0, len(l) - 1, 2)]
    if all(x == sums[0] for x in sums) and all(x in l for x in range(1, 1 + len(l))):
        k = [(str(l[x]) + str(l[x+1]) + str(l[(x+3) % len(l)])) for x in range(0, len(l) - 1, 2)]
        i = min(enumerate(map(int, k)),key=lambda x: x[1])[0]
        k = k[i:] + k[:i]
        return int(''.join(k))
    return 0
m = 0
for x in itertools.permutations(range(1, 11)):
    if x.index(10) & 1 == 1:
        continue
    n = magicNgon(x)
    if n > m:
        m = n
print(m)
