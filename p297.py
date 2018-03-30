# for some reason doesn't quite work for fib(i), but works
# for everything else.
from combinatorics import fib
def zsum(n):
    if n < 4:
        return n
    i = 3
    sol = [0, 1, 2]
    while n > fib(i+1):
        sol[0] = sol[1]
        sol[1] = sol[2]
        sol[-1] = sol[0]+ sol[1] + fib(i)
        i += 1
    return sol[1] + zsum(n-fib(i))+n-fib(i)+1
print(zsum(10**17-1))