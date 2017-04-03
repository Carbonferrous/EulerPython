from combinatorics import polynomial, combinations
from random import sample
#
#s = 0
#t = 0
#b = []
#for i in range(7):
#    c = polynomial()
#    for j in range(11):
#        k = [0]*7
#        k[i] = j
#        c += {tuple(k): 1}
#    b += [c]
#print('polynomials generated')
#p = polynomial()
#p += {tuple([0]*7):1}
#for c in b:
#    p = p*c
#    keystoremove = []
#    for k in p:
#        if sum(k) > 20:
#            keystoremove += [k]
#    for k in keystoremove:
#        del p[k]
#    keystoremove = []
#    print('Hello')
#s = 0
#t = 0
#for k in p:
#    if sum(k) == 20:
#        t += p[k]
#        s += (10-k.count(0))*p[k]
#print(s, t, s/t)

#for p in range(2, 8):
#    n = ((b**p)[20])*combinations(7, p)
#    s += p*n
#    print(p, n, (b**p)[20], combinations(7, p), s)
#print(s)
#print('{0:.9f}'.format(s/195195))

tr = 0
pop = [1, 2, 3, 4, 5, 6, 7]*10
x = 0
while tr < 10**10:
    x += len(list(set(sample(pop, 20))))
    tr += 1
print('{0:.9f}'.format(x/tr))