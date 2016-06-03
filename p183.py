import math

def k(n):
    return int(round(n/math.e, 0)+.5)

def d(n):
    t = k(n)
    t = t // math.gcd(t, n)
    while t % 2 == 0:
        t = t // 2
    while t % 5 == 0:
        t = t // 5
    if t == 1:
        return -n
    return n

print(sum(d(n) for n in range(5, 10**4+1)))
