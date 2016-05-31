import itertools

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

count = 0
for y, z in itertools.product(range(1, 1801), repeat = 2):
    if lcm(y, z) != 900: continue
    for x in range(1, 1801):
        if lcm(x, y) != 72: continue
        if lcm(x, z) != 600: continue
        count += 1
        print(x, y, z)
print(count)
