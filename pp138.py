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

def sol(n):
    return sum(fib(n)[0] for n in range(9, 6*n+3 + 1, 6))>>1

#for i in range(int(input())):
#    print(sol(int(input())))
