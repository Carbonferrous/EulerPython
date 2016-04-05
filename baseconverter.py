def value2base(n, base):
    b = ""
    while n >= base:
        b = str(n % base) + b #need to concider characters in different bases
        n = n // base
    return str(n) + b
def base2value(s, base):
    n = 0
    s = str(s)
    c = 0
    while len(s) > 0:
        n += int(s[-1]) * base ** c #same here
        c += 1
        s = s[:-1]
    return n
def base2base(s, b1, b2):
    s = str(s)
    if b1 <= 10 and b2 <= 10:
        return value2base(base2value(s,b1),b2)
    return 0
print(value2base(214, 3))
print(base2value(364,7))
print(base2base(500,10,2))
