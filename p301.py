import combinatorics
def b(n):
    return '{:b}'.format(n)
for i in range(10):
    c = 0
    for n in range(1, 2**i+1):
        if b(n).count('11') == 0:
            c += 1
    print(i, c, combinatorics.fib(i+2))
print('fibonacci')
print(combinatorics.fib(32))