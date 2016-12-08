def f(x):
    return int(1420000000.2794/2**(x**2))/10**9
u = -1
n = f(u)
for i in range(100000):
    u = n
    n = f(u)
print(u+n)
