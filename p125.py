import math
def ispalendrome(n):
    n = str(n)
    return n == n[::-1]

limit = 10**8

squares = []
s = 0
for i in range(int(math.sqrt(limit))+1):
    s += i ** 2
    squares += [s]

s = 0
n = 0
found = []
for i in range(len(squares)):
    for j in range(i-1):
        n = squares[i] - squares[j]
        if ispalendrome(n) and n < limit and n not in found:
            s += n
            found += [n]
print(s, len(found))
