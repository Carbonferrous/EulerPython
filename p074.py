import math
def fact(n):
    return sum(math.factorial(int(c)) for c in str(n))
loops = {1:1, 2:1, 145:1, 40585:1, 169:3, 363601:3, 1454:3, 871:2, 45361:2, 872:2, 45362:2}
total = 0
for n in range(1000000):
    count = 0
    t = n
    while t not in loops:
        t = fact(t)
        count += 1
    count += loops[t]
    if count == 60:
        total += 1
print(total)
