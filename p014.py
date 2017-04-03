#from math import log
#def collatz(n, l=-1):
#    s = ''
#    sl = [n]
#    while not l == 0 and not n == 1:
#        if n % 2 == 0:
#            n = n//2
#            s += 'd'
#        else:
#            n = (3*n+1)//2
#            s += 'u'
#        sl += [n]
#        l -= 1
#    return s, n, sl
# uu is not a valid string, d...d is power of 2
# it takes int(log(x, 2))+1 terms to identify the numbers below x (chinese rem)
#l = 32
#setofpaths = {}
#for i in range(1, l+1):
#    path, left, npath = collatz(i, int(log(l, 2))+1)
#    if path in setofpaths:
#        print(i, path, setofpaths[path])
#    else:
#        setofpaths[path] = i
#    print(i, '{0:b}'.format(i), path, left, max(npath))
#print(len(setofpaths))
c = {1:0}
for x in range(1, 1000000+1):
    n = 0
    i = x
    while not i == 1 and i not in c:
        if i % 2 == 0:
            i = i//2
        else:
            i = 3*i+1
        n += 1
    c[x] = n + c[i]
m = 0
mk = 1
for k in c:
    if c[k] > m:
        mk = k
        m = c[k]
print(mk)