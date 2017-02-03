# b10**n+a10**n=pab
# a <= b
# b 2**n 5**n = 0 mod a
# a 2**n 5**n = 0 mod b
#
#case a == b
#2**(n+1)*5**n=p*a
#
#(n+2)(n+1)
#possibilities
#
#case a < b
#a 2**n 5**n = 0 mod b
#pk 2**n 5**n = 0 mod qk
#p 2**n 5**n = 0 mod q
#q10**n+p10**n=Ppkq

#case p == 1 or b = qa
#q != 1
#(q+1)10**n=Pqk
#q = 2**k 5**l where k,l <= n
#Then
#(2**k*5**l+1) 2**(n-k) 5**(n-l) = Pk
#(2**n*5**n+2**(n-k)*5**(n-l)) = Pk

#for k in range(n+1):
#    for l in range(n+1):
#        if k == 0 and l == 0:
#            continue
#        s += (n-k+1)*(n-l+1)*numDivisor(2**k*5**l+1)
#
#case p != 1
#p < q
#2**i 5**j < 2**k 5**l
#i or k == 0
#j or l == 0
#i or j != 0
#2**(n+i) 5**(n+j) = 0 mod 2**k 5**l
#2**(n+k) 5**(n+l) = 0 mod 2**i 5**j
#a10**n+b10**n=Pab
#a = pK and b = qK
#p10**n+q10**n=PpqK
#p = 2**i 5**j and q = 2**k 5**l and gcd(p, q) == 1, so
#i or k == 0
#j or l == 0
#i or j != 0
#Thus,
#1.  p = 2**i and q = 5**l
#2.  p = 5**j and q = 2**k
#Therefore:
#1.    2**(n+i)*5**n+2**n*5**(n+l)=PK2**i*5**l
#      2**(n-i)*5**(n-l)*(2**i+5**l)=PK
#        (n-i+1)(n-l+1)*numDivisor(2**i+5**l)
#2.    2**(n-k)*5**(n-j)*(2**k+5**j)=PK
#        (n-k+1)(n-j+1)*numDivisor(2**k+5**j)
#For powers of 2
#n >= k-i
#n >= i-k
#For powers of 5
#n >= l-j
#n >= j-l
#case p is a power of 2
#for i in range(1, n+1):
#    for l in range(1, n+1):
#        if 2**i < 5**l:
#            add 1
#case p is a power of 5
#for j in range(1, n+1):
#    for k in range(1, n+1):
#        if 5**j < 2**k:
#            add 1
import math
import numbertheory
from numbertheory import numDivisor
s = 0
for n in range(1, 10):
    s += (n+2)*(n+1)
    for k in range(n+1):
        for l in range(n+1):
            if k == 0 and l == 0:
                continue
            s += numDivisor(2**n*5**n+2**(n-k)*5**(n-l))
    for i in range(1, n+1):
        for l in range(1, n+1):
            if 2**i < 5**l:
                s += (n-i+1)*(n-l+1)*numDivisor(2**i+5**l)
    for j in range(1, n+1):
        for k in range(1, n+1):
            if 5**j < 2**k:
                s += (n-k+1)*(n-j+1)*numDivisor(2**k+5**j)
print(s)
