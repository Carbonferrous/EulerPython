#solving ((5b+-4)/2)^2-5L^2 = -1 with pell's equation and contfrac of sqrt(5)
#then realizing that each term is f(6n+3)//2
import numbertheory
def f(n):
    return numbertheory.contfrac2real([2]+[4]*(n-1))
def sol(a):
    return (a[0]*2)%5 == 1 or (a[0]*2)%5 == 4
s = 0
numFound = 0
x = 3
while numFound < 12:
    if sol(f(x)):
        s += f(x)[1]
        print(numFound+1, x, f(x), s)
        numFound += 1
    x += 2
print(s)
def sums(n):
    return sum(numbertheory.fib(6*n+3)//2 for n in range(1, n + 1))
print(sums(12))
