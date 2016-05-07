from fractions import gcd
def pyth(n, m):
    return(n**2 - m**2, 2*n*m, n**2 + m**2)
#sum(pyth(n, m))
#2n**2+2nm = 2n(n+m)
count = 0
for n in range(1, 7072):
    for m in range(1, n):
        if n**2+n*m > 50000000:
            break
        if gcd(n, m) != 1 or (n**2+m**2) % abs(n**2-m**2-2*n*m) != 0:
            continue
        count += 50000000//(n**2+m*n)
        if 50000000 % (n**2+m*n) == 0:
            count -= 1
            print(n, m)
print(count)
