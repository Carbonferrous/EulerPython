from numbertheory import totientList

t = totientList(10**7)
next(t)
next(t)
m = 5
for n in range(2, 10**7):
    k = next(t)
    sk = str(k)
    if len(sk) < len(str(n)):
        sk += '0'
    if n/k < m and sorted(sk) == sorted(str(n)):
        m = n/k
        print(n, k, n / k)
print(m)
