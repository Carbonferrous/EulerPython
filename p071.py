from fractions import gcd
n = 2
d = 5
while d + 7 <= 1000000:
    n = n + 3
    d = d + 7
print(n,d)
