def int2base(x, base):
    digits = []
    while x:
        digits += [x % base]
        x = x // base
    return digits

def tri(n):
    return n * (n + 1) // 2

def product(l):
    x = 1
    for i in l:
        x *= i + 1
    return x

def countstuff(n, base):
    s = 0
    exp = 0
    digits = int2base(n, base)
    for x in range(len(digits)):
        s += tri(digits[x]) * tri(base) ** exp * product(digits[x+1:])
        exp += 1
    return s

print(countstuff(10**9, 7))
