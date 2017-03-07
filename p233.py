import numbertheory
import itertools
#N = 2*n
#s = 4 + 8 * cs
#x**2+y**2=2*n**2
p = list(c for a, b, c in itertools.islice(numbertheory.pythag(), 1000000))
p.sort()
print(p[-1])
t = 0
asdf = 0
for n in range((10**11)//2+1):
    count = 0
    for c in p:
        if c > n:
            break
        if n % c == 0:
            count += 1
    if count == 52:
        t += 1
        asdf += 2*n
print(t, asdf)
#for x in range(n, int(math.sqrt(2)*n)):
#    for y in range(0, n+1):
#        if x**2+y**2==2*n**2:
#            print(x, list(numbertheory.factor(x)), ':', y, list(numbertheory.factor(y)))
#            u = (x+y)
#            v = (x-y)
#            g = math.gcd(u, v)
#            u, v = u//g, v//g
#            print(u, v, int(math.sqrt(u**2+v**2+.5)))