import numbertheory

p = list(numbertheory.primeList(100000000))
s = set(p)
d = dict(list((i, 0) for i in p))
assert len(p) == len(s) and len(p) == len(d)
print('primes generated')
print('start list')
for i in p:
    pass
print('end list')
print('start set')
for i in s:
    pass
print('end set')
print('start dictionary')
for i in d:
    pass
print('end dictionary')
