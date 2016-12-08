# b = (sqrt(8*r**2+1)+2*r+1)/2
# m**2 - 8*r**2 == 1
from numbertheory import pell
from math import sqrt
p = pell(8)
for m, r in p:
    b = int(sqrt(8*r**2+1)+2*r+1)//2
    if b + r > 10**12:
        break
print(b, r, b + r)
