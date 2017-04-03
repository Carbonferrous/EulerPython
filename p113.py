amem = {}
dmem = {}


def d(i, v):
    if i == 1:
        return 1
    if not (i, v) in dmem:
        dmem[(i, v)] = sum(d(i-1, j) for j in range(v+1))
    return dmem[(i, v)]


def a(i, v):
    if i == 1:
        return 1
    if not (i, v) in amem:
        amem[(i, v)] = sum(a(i-1, j) for j in range(v, 10))
    return amem[(i, v)]


def s(l):
    if l == 1:
        return 9
    t = s(l-1)
    for i in range(1, 10):
#       print(l, i, a(l, i) + d(l, i) - 1)
        t += a(l, i) + d(l, i) - 1
#   print(l, t)
    return t
print(s(100))
