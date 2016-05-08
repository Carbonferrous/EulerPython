#solving (5n+7)^2-5k^2 = 44 with pell's equation and contfrac of sqrt(5)
import numbertheory
def f(n):
    return numbertheory.contfrac2real([2]+[4]*(n-1))


