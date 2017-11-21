#solving (5n+7)^2-5k^2 = 44 with pell's equation and contfrac of sqrt(5)
#Generating function of G is (-3x^2-x)/(x^2+x-1)
#n = G(x)
#x = (sqrt(5n**2+14*n+1)-n-1)/(2(n+3))
#5*n**2+14*n+1 = k**2
#(5n+7)^2-5k^2 = 44
#n  5*n+7  k
#0  7      1
#2  17     7
#5  32     14
#21 112    50
#42 217    97
#152 767   343
##Differences are f(4), 2*f(6), f(8), 2*f(10), ...
##A(n) is the nth golden nugget
##f(n) is the nth fibonacci number
##A(n) = 7*A(n-2)-A(n-4)+7
##A(n) = 2*f(2)+f(4)+2*f(6)+f(8)+2*f(10) + ...
##A(n) = sum(f(4*i+2) for i in range((n+1)//2)) + sum(f(2*i) for i in range(1, n+1))
##A(n) = sum(f(4*i+2) for i in range((n+1)//2)) + f(2*n+1) - 1
##Consider the first term
##S = f(2) + f(6) + f(10) + f(14) + ... + f(2*(n - 1))(for even n) + f(2*n)(for odd n)
##p = n for odd n and n-1 for even n
##S = fib(2*p)+fib(2*p-3)-fib(p-2)**2
##S = fib(2*p+1)-fib(p)**2
##A(n) = f(2*p+1) + f(2*n+1) - 1 - f(p)**2
##if n is odd
##A(n) = f(2*n+1) + f(2*n+1) - 1 - f(n)**2
##A(n) = 2*(f(n+1)**2+f(n)**2) - 1 - f(n)**2
##A(n) = 2*f(n+1)**2 + f(n)**2 - 1
##if n is even
##A(n) = f(2*(n-1)+1) + f(2*n+1)-1-f(n-1)**2
##A(n) = f(2*n-1) + f(2*n+1) - 1 - f(n-1)**2
##A(n) = f(n)**2 + f(n-1)**2 + f(n+1)**2 + f(n)**2 - 1 - f(n-1)**2
##A(n) = 2*f(n)**2 + f(n+1)**2 - 1
##
##Sol(n) = A(1) + A(2) + A(3) + A(4) + ... + A(n)
##Sol(n) = (2*f(2)**2 + f(1)**2 - 1) + (2*f(2)**2 + f(3)**2 - 1) + (2*f(4)**2 + f(3)**2 - 1) + (2*f(4)**2 + f(5)**2 - 1) + ... + (2*f(n+1)**2 + f(n)**2 - 1)(odd) + (2*f(n)**2 + f(n+1)**2 - 1)(even)
##Sol(n) + 1 = -n + 2*f(1)**2 + 4*f(2)**2 + 2*f(3)**2 + 4*f(4)**2 + 2*f(5)**2 + ... + (4*f(n-1) + 2*f(n)**2 + 2*f(n+1)**2)(odd) + (2*f(n-1) + 4*f(n)**2 + f(n+1)**2)(even)
##if n is odd
##Sol(n) + 1 + n = 2*(f(n+1)*f(n+2)) + 2*sum(f(2*i)**2 for i in range(1, n))
##Sol(n) + 1 + n = 2*(f(n+1)*f(n+2)) + 2*(f(4*n-2)-2*n-1)/5
##if n is even
##Sol(n) + 1 + n = 2*(f(n)*f(n+1)) + f(n+1)**2 + 2*sum(f(2*i)**2 for i in range(1, n+1))
##Sol(n) + 1 + n = 2*(f(n)*f(n+1)) + f(n+1)**2 + 2*(f(4*n+2)-2*n-1)/5
##
##f(2*(2*n-1)) = something complicated
##f(2*(2*n+1)) =


##A(n) = f(2*(n+1)//2+1)*f(2*(n+1)//2+3) - 1 + f(2*n+1) - 1
##m = n+1 for odd and n for even
##A(n) = f(m-1)*f(m+1) + f(2*n+1) - 2

##Sol(n) = A(1) + A(2) + A(3) + A(4) + ... + A(n)
##Sol(n) = -2*n + sum(f(2*i+1) for i in range(1, n + 1)) + f(1)f(3) + f(1)f(3) + f(3)f(5) + ... + f(n)f(n+2)(odd) + f(n-1)f(n+1)
##Sol(n) = -2*n - f(1) + sum(f(2*i+1) for i in range(n + 1)) + 2*(f(1)f(3) + f(3)f(5) + ... + f(n-2)f(n)(odd) + f(n-1)f(n+1)(even)) + f(n)f(n+2)(odd)
##Sol(n) = -2*n - f(1) + f(2*n+2) + 2*(f(1)f(3) + f(3)f(5) + ... + f(n-2)f(n)(odd) + f(n-1)f(n+1)(even)) + f(n)f(n+2)(odd)
##Sol(n) = -2*n - 1 + fib(2*n+2) + sum(fib(2*i-1)*fib(2*i+1) for i in range(1, n//2+1)) + sum(fib(2*i-1)*fib(2*i+1) for i in range(1, n//2+n%2+1))
##Sol(n) = -2*n - 1 + fib(2*n+2) + sum(fib(2*i)**2 + 1 for i in range(1, n//2+1)) + sum(fib(2*i)**2 + 1  for i in range(1, n//2+n%2+1))
##Sol(n) = -n - 1 + fib(2*n+2) + sum(fib(2*i)**2 for i in range(1, n//2+1)) + sum(fib(2*i)**2 for i in range(1, n//2+n%2+1))

##fib(2*n) + 5*fib(2*n+2) + fib(2*n+4)
##2*fib(2*n) + fib(2*n + 1) + 4*fib(2*n+2) + fib(2*n+4)
##2*fib(2*n) + 2*fib(2*n+2) + 2*fib(2*n+4)
##2*(fib(2*n) + fib(2*n+2) + fib(2*n+4))



from combinatorics import fib, _fib

def A1(n):
    return sum(fib(4*i+2) for i in range((n+1)//2)) + sum(fib(2*i) for i in range(1, n+1))

def A2(n):
    p, q = _fib(n)
    if n % 2 == 1:
        return 2*q**2 + p**2 - 1
    return 2*p**2 + q**2 - 1

def A3(n):
    #return sum(fib(4*i+2) for i in range((n+1)//2)) + fib(2*n+1) - 1
    if n < 1:
        return 0
    m = n + (n%2)
    return fib(m-1)*fib(m+1) + fib(2*n+1) - 2

def sol1(n):
    return sum(A3(i) for i in range(1, n + 1))

def sol3(n):
    if n % 2 == 0:
        return 7*(fib(2*n+2) - n - 1)//5
    return (8*fib(2*n+2) - 7*n - 7)//5


print(sol3(30))

for i in range(1, 31):
    if sol3(i) != sol1(i):
        print(i, sol1(i), sol3(i))

##for n in range(1, 31):
##    print(n, 2*(n//2+n%2))
