from math import gcd
p = 1009
q = 3643
phi = (p-1)*(q-1)
total = 0
m = 9
for e in range(2, phi):
    if not gcd(e, phi) == 1:
        continue
    if gcd(e-1, p-1) == 2 and gcd(e-1, q-1) == 2:
        total += e
print(total)
