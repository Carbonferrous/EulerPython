from numbertheory import farey
import math
squares = {i**2:i for i in range(1, 346)}

s = 0
sol = []
for a, b in farey(346):
    k = a**2 + b**2 - a*b
    if k in squares and 346 > 2*a+b:
        s += 346//squares[k]
        print(a, b, squares[k], s)
        sol += [(a, b, squares[k])]
print(s)
print(sol)
