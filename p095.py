import math
import itertools
import numbertheory

LIMIT = 1000000
amicable = list(numbertheory.sumDivisorList(LIMIT*2))

c = [-1, -1] + [0]*LIMIT
for x in range(2, LIMIT + 1):
    t = [x]
    if c[x] == 0:
        a = amicable[x]-x
        while a != x and (a not in t) and a < LIMIT and c[a] != -1:
            t += [a]
            a = amicable[a]-a
        if a == x:
            for b in t:
                c[b] = 1
            print(t)
        else:
            if a > LIMIT or a == 1:
                for b in t:
                    c[b] = -1
            c[x] = -1

