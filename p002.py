def evenfibgen():
    a, b, c = 2, 8, 34
    while True:
        yield a
        a, b = b, c
        c = 4 * b + a

s = 0
a = evenfibgen()
c = next(a)
while c < 4000000:
    s += c
    c = next(a)
print(s)
