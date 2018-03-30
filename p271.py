#consider n = product(p_i**1), where p_i are distinct primes
#for each p_i, there are two solutions to: 
#       x**3 == 1 mod pi (eq 1)
#The solutions are a_i and a_i**(-1) = a_i**2 mod p_i
#moreover, there are only solutions if p_i % 6 == 1, let these primes be p_si
#9 can also act as a prime basis
#rewrite n = product(p_si**1)*product(p_k**1)
#There are 3**i (or 3**i-1 in this problem) solutions to
#x**3 == 1 mod n where 0<x<n
#x satisfies the following modular identities
#x == 1 mod p_k for each k
#x == 1, a, or a**2 for each p_si
#each x can then be enumerated by chinese remainder theorem


from numbertheory import egcd

from numbertheory import primeList


def chineseremainder(crt):
    nx = 1
    ax = 0
    x = 0
    for n, a in crt:
        g, m1, m2 = egcd(nx, n)
        if not g == 1:
            raise Exception('not all coprime')
        x = ax*m2*n + a*m1*nx
        nx *= n
        ax = x % nx
    return x % nx

mods = {}
i = 0
# for each prime determine basis
for p in primeList(44):
    if p % 6 == 1:
        i += 1
        for x in range(2, p):
            if pow(x, 3, p) == 1:
                mods[p] = [1, x, x**2%p]
                print(p, mods[p])
                break
    else:
        mods[p] = [1]
# calculate n
n = 1
for p in mods:
    n *= p
#######
#i = 2
#n = 7*13
#mods = {7:[1, 2, 4], 13:[1, 3, 9]}
#######
# construct chinese remainder theorem and then add to sum
s = -1
c = 0
while c < 3**i:
    crt = []
    j = c
    for p in mods:
        if len(mods[p]) == 1:
            crt += [(p, mods[p][0])]
        else:
            crt += [(p, mods[p][j%3])]
            j = j//3
    a = chineseremainder(crt)
    s += a
    c += 1
print(s)