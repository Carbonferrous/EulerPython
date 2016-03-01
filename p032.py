import math
import itertools

prod = set()
perm = list(''.join(x) for x in itertools.permutations("123456789"))

for p in perm:
    for s in range(1,5):
        if int(p[:s])*int(p[s:5])==int(p[5:]):
            prod.add(int(p[5:]))
print(sum(prod))
