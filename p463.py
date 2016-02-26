def s(n):
    a = 0
    for x in range(1, n+1):
        a += int("{0:b}".format(x)[::-1],2)
    return a

def s2(n):
    s = 1
    for x in range(1, n + 1):
        s += 1 << 2 * (x - 1)
    return s
