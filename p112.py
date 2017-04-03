def isnotbouncy(n):
    n = str(n)
    return all(n[i] <= n[i+1] for i in range(len(n)-1)) or all(n[i] >= n[i+1] for i in range(len(n)-1))
n = 0
c = 0
while 100*c <= 99*n:
    n += 1
    if not isnotbouncy(n):
        c += 1
print(c, n-1)