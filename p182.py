from numbertheory import egcd, modinv
import numbertheory
from math import gcd
class RSA:
    def __init__(self, n = None, publicKey = None):
        self.n = n
        self.publicKey = publicKey
##    def genrandprime(self, digits):
##        if digits == 1:
##            return 2
##    def host(self, p, q):
##        self.n = p * q
##        self.phi = (p-1)*(q-1)
####        find d - private key
####            e - public key
####            such that d * e == 1 mod phi and gcd(e, phi) == 1
####        self.privateKey = modinv(self.publicKey, self.phi)
    def numUnconcealed(self, p, q):
        return (gcd(self.publicKey - 1, p - 1) + 1) * (gcd(self.publicKey - 1, q - 1) + 1)
    def encrypt(self, message):
        if not(0 <= message and message < self.n):
            raise ValueError('message not in valid range')
        return pow(message, self.publicKey, self.n)
    def decrypt(self, cyrptogram):
        if not(0 <= cyrptogram and cyrptogram < self.n):
            raise ValueError('cryptogram not in valid range')
        return pow(cyrptogram, self.privateKey, self.n)

p = 1009
q = 3643
phi = (1009-1)*(3643-1)
total = 0
for e in range(2, phi):
    if not gcd(e, phi) == 1:
        pass
    if gcd(e-1, p-1) == 1 and gcd(e-1, q-1) == 1:
        total += e
print(total)
