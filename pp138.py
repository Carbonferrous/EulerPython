from math import sqrt
def fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib(n >> 1)
        c = a * ((b << 1) - a)
        d = a * a + b * b
        if n & 1 == 0:
            return (c, d)
        else:
            return (d, c + d)

def sol1(n):
    return sum(fib(n)[0] for n in range(9, 6*n+3 + 1, 6))>>1

#f(6n+3) = 5f(6(n-1)+3)+8f(6(n-1)+3+1)
#f(6n+3+1) = 8f(6(n-1)+3)+13f(6(n-1)+3+1)
#f(6+3)+f(6*2+3)+...+f(6*(n-1)+3)+f(6n+3)
def sol2(n, x):
    a = 17
    b = 55
    s = 0
    for i in range(n):
        s += a
        a, b = 5*a + (b<<2), (a<<4) + 13*b
        a, b = a, b
    return s

def sol3(n, x=10**9+7):
    m = n
    y = x
    a = 1
    b = 17
    s = 0
    for i in range(m):
        a, b = b, 18*b-a
        b = b%y
        s += a
    return s%y

#calculates solution directly
def sol4(n):
    a = 0
    b = 17
    for i in range(n):
        a, b = b, 18*b-a+16
    return a

#print(sol4(1234567, 10**9+7))

#for i in range(int(input())):
#    print(sol(int(input())))