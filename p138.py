#solving ((5b+-4)/2)^2-5L^2 = -1 with pell's equation and contfrac of sqrt(5)
import numbertheory
def f(n):
    return numbertheory.contfrac2real([2]+[4]*(n-1))
def sol(a):
    return (a[0]*2)%5 == 1 or (a[0]*2)%5 == 4
s = 0
numFound = 0
x = 2
while numFound < 12:
    if sol(f(x)):
        s += f(x)[1]
        print(x, f(x), s)
        numFound += 1
    x += 1
print(s)
