from numbertheory import isPrime, factor
def t(n):
    return 2*n**2-1

for m in range(2, 500):
    for n in range(m + 1):
        if t(n) % m == 0:
            print(n, m)
            break

