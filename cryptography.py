import random, math
from numbertheory import isPrime, primeList, modinv
from math import gcd
def randprime(bits, safeness = 0):
    rng = random.SystemRandom()
    i = 0
    while len('{0:b}'.format(i)) != bits:
        i = rng.getrandbits(bits)
    i += 1 - (i % 2)
    pList = list(primeList(1000))
    while True:
        if all(i % p not in ([0] + [(p-(2**n-1))//2**n for n in range(safeness + 1)]) for p in pList) and all(isPrime(2**n*i+2**n-1) for n in range(safeness + 1)):
            return i
        i += 2

def getkeys(p, q):
    phi = (p - 1) * (q - 1)
    e = 2**16 + 1
    if gcd(e, phi) == 1 and gcd(e-1, p-1) == 2 and gcd(e-1, q-1) == 2:
        return (e, modinv(e, phi))
    rng = random.SystemRandom()
    while True:
        e = rng.randint(3, int(math.sqrt(phi//gcd(p-1, q-1))))
        if gcd(e, phi) == 1 and gcd(e-1, p-1) == 2 and gcd(e-1, q-1) == 2:
            return (e, modinv(e, phi))
    
def i2osp(x, xLen):
    if x >= 256 ** xLen:
        raise ValueError('integer too large')
    b = bytes()
    for i in range(xLen):
        b = bytes([x % 256]) + b
        x = x // 256
    return b
def os2ip(x):
    i = 0
    for b in x:
        i *= 256
        i += b
    return i

def rsaep(n, e, m):
    if not (-1 < m and m < n):
        raise ValueError('message representative out of range')
    return pow(m, e, n)
def rsadp(n, d, c):
    if not (-1 < c and c < n):
        raise ValueError('ciphertext representative out of range')
    return pow(c, d, n)
def rsasp1(n, d, m):
    if not (-1 < m and m < n):
        raise ValueError('message representative out of range')
    return pow(m, d, n)
def rsavp1(n, e, s):
    if not (-1 < s and s < n):
        raise ValueError('signature representative out of range')
    return pow(s, e, n)

##def rsaesoaepencrypt(n, e, m, l = ''):
##    #length check
##    if len(str(l)) > hashInput:
##        raise ValueError('label too long')
##    if len(str(m)) > len(str(n)) - 2 * len(str(h)) - 2:
##        raise ValueError('message too long')
##    lHash = Hash(l)
##    PS = '0' * (len(str(m)) - len(str(n)) - 2 * len(str(h)) - 2)
##    DB = lHash + PS + '1' + m
##    seed = randomint of size hLen
##    dbMask = MGF(seed, k - hLen - 1)
##    
