def fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib(n // 2)
        c = (a * (2*b - a))%(10**9+7)
        d = (a**2 + b**2)%(10**9+7)
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)
def sol(n):
    i = n + 1
    if i % 2 == 1:
        return (800000007*(fib(2*i)[0] - i))%(10**9+7)
    return (400000003*(8*fib(2*i)[0] - 7*i))%(10**9+7)

s = ''
for t in range(int(input())):
    l,r = map(int, input().split(' '))
    s += str((sol(r)-sol(l-1))%(10**9+7)) + '\n'
print(s)
