from numbertheory import modinv
def zero(n):
    s = 0
    while n > 1:
        s += n//5
        n = n//5
    return s
def fact(n):
    lim = 10**(zero(n) + 5)
    s = 1
    for i in range(1, n+1):
        s = s*i
        s = s % lim
    return s//10**zero(n)

print(fact(1000000))