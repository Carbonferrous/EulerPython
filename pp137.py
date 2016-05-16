##f(3) + f(7) + f(11) + ... + f(4*(n - 1) + 3) = f(2*n+1) * f(2*n)
##1      2      3       
from numbertheory import _fibmod
def sol(n):
    p, q = _fibmod(2*n, 10**9 + 7)
    return (p*q)%(10**9+7)
s = ''
for t in range(int(input())):
    s += str(sol(int(input()))) + '\n'
print(s)
