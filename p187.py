import numbertheory as asdf
import math

p = list(asdf.primeList(10**8))
s = 0
for prime in p:
    if prime * 2 < 10 ** 8:
        foo = list(asdf.primeList(10**8//prime))
        for n in foo:
            if n >= prime:
                s += 1
print(s)
