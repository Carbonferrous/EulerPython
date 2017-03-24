# gk = 1 for 0<=k<=1999
# gk = g(k-2000)+g(k-1999) for k>=2000
# r**k = r**(k-2000) + r**(k-1999)
# r**2000 = 1 + r
# r**2000 - r - 1 = 0
l = {}


def g2(n, m):
    if 0 <= n and n <= 1999:
        return 1
    if n in l:
        return l[n]
    else:
        k = g(n, m)
        l[n] = k
        return l[n]


def g(n, m):
    if 0 <= n and n <= 1999:
        return 1
    return (g2(n-2000, m) + g2(n-1999, m)) % m


def g3(n, m):
    a = [0]*2001
    a[n % 2000] = 1
    i = n//2000*2000
    while i >= 2000:
        a = [a[0]] + list((a[j] + a[j-1]) % m for j in range(1, 2001))
        a[0] += a[2000]
        a[1] += a[2000]
        a[2000] = 0
        i -= 2000
    print(a[:5], a[-5:])
    return sum(a[:-1]) % m
m = 10**5
#for n in range(10):
#    print(g3(2000*n, m))
print(g3(2000*1998+3, m))
#print(g3(2000*2000, m))
#print(g3(2000*2001, m))
#print(n, g3(n, m), g(n, m))
