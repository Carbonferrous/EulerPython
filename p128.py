from numbertheory import isPrime
l = [1, 2]
# n = ['0',
#     '322224',
#     '312121212124',
#     '311211211211211214',
#     '311121112111211121112114']
# PD(1s)<=2
# PD(2s)<=2
# s3 = (3*n**2-3*n+2, 6*n+1, 6*n-1, 12*n+5)
# s4 = (3*n**2+3*n+1, 12*n-7, 6*n-1, 6*n+5)
n = 2
while len(l) < 2000:
    if isPrime(6*n+1) and isPrime(6*n-1) and isPrime(12*n+5):
        l += [3*n**2-3*n+2]
    if isPrime(12*n-7) and isPrime(6*n-1) and isPrime(6*n+5):
        l += [3*n**2+3*n+1]
    n += 1
print(l[1999])
