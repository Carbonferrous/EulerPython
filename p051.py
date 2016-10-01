import numbertheory as nt
def rep(n, s):
##    if '*' not in n:
##        return int(nt.isPrime(int(n)))
    t = 0
    for i in range(s, 10):
        if nt.isPrime(int(n.replace('*', str(i)))):
            t += 1
    return t

def search(s):
    for n in nt.primeList(1000000):
        n = str(n)
        for i in n:
            if rep(n.replace(str(i), '*'), int(i == n[0])) == s:
                return n.replace(str(i), '*')
    return 0
        
print(list(search(i) for i in range(1, 9)))
