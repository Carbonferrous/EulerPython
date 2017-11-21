#(a+d)**2 - a**2 - (a-d)**2 = n
#4*a*d-a**2 = n
#n % 4 in [3, 0]
#a*(4*d-a) = n
#d = (n//a + a)
#d % 4 == 0 and d < a
#d = (n+a**2)/(a*4)
#a > 0, d > 0, a//4 < d < a <= n
#
#n < 3*a**2
#a > sqrt(n/3)
from numbertheory import divisorList
limit = 1000000
goal = 10
count = 0
def sol(n):
    c = 0
    for a in divisorList(n):
        d = n//a + a
        if d % 4 == 0 and d < 4*a:
            c += 1
    return c

for n in range(3, limit, 4):
    c = sol(n)
    if c == goal:
        count += 1
print(count)
for n in range(4, limit, 4):
    c = sol(n)
    if c == goal:
        count += 1
print(count)
