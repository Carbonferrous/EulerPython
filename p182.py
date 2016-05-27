from numbertheory import egcd, modinv, primeList, isPrime
from math import gcd
import random
##let a SG2 prime be a prime where 2*p+1 and 4*p+3 are also prime
##let a S2 prime be a prime of the form 4*p+3 where p is a SG2 prime
##n != 0 mod p
##n != (p-1)/2 mod p
##n != (p-3)/4 mod p

def genrandprime(bits):
    b = bits
    rng = random.SystemRandom()
    n = 0
    while b != len("{0:b}".format(n)):
        n = rng.getrandbits(b)
        n += 1 - (n % 2)
    while True:
        if all(n % p not in [0, (p-1)//2,(p-3)/4] for p in primeList(1000)) and (isPrime(n, trialDivision = 0) and (isPrime(2*n+1, trialDivision = 0) and isPrime(4*n+3, trialDivision = 0))):
            if isPrime(n, trialDivision = 0, millerRabin = 100000) and isPrime(2*n+1, trialDivision = 0, millerRabin = 100000) and isPrime(4*n+3, trialDivision = 0, millerRabin = 100000):
                return n
        else:
            n += 2
def lcm(a, b):
    return a//gcd(a, b)*b
##properties of p and q
##p and q should be S2 primes and are thus of form 4*p1+3 and 4*q1+3
##p+1 and q+1 should have large prime factors

class RSA:
    def __init__(self, n = None, publicKey = None):
        self.n = n
        self.publicKey = publicKey
##    def host(self, p, q):
##        self.n = p * q
##        phi = (p-1)*(q-1)
##        for e in range(5,sqrt(lcm(p-1, q-1)))
####        find e - public key such that
####            gcd(e, phi) == 1
####        self.privateKey = modinv(self.publicKey, phi)
##    def numUnconcealed(self, p, q):
##        return (gcd(self.publicKey - 1, p - 1) + 1) * (gcd(self.publicKey - 1, q - 1) + 1)
    def encrypt(self, message):
        if not(0 <= message and message < self.n):
            raise ValueError('message not in valid range')
        if self.publicKey == None:
            raise ValueError('no public key')
        if self.n == None:
            raise ValueError('no integer n')
        return pow(message, self.publicKey, self.n)
    def decrypt(self, cyrptogram):
        if not(0 <= cyrptogram and cyrptogram < self.n):
            raise ValueError('cryptogram not in valid range')
        if self.privateKey == None:
            raise ValueError('no private key')
        if self.n == None:
            raise ValueError('no integer n')
        return pow(cyrptogram, self.privateKey, self.n)
    def sign(self, messsage):
        return decrypt(message)
    def verify(self, cryptogram):
        return encrypt(cryptogram)

##p = 1009
##q = 3643
##phi = (p-1)*(q-1)
##total = 0
##m = 9
##for e in range(2, phi):
##    if not gcd(e, phi) == 1:
##        continue
##    if gcd(e-1, p-1) == 2 and gcd(e-1, q-1) == 2:
##        total += e
##print(total)
