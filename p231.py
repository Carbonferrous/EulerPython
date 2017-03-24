from combinatorics import factfact

s = 0
for p, e in factfact(20000000):
    s += p*e
for p, e in factfact(15000000):
    s -= p*e
for p, e in factfact(20000000-15000000):
    s -= p*e
print(s)
