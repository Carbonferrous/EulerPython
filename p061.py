def polygon(s, n):
    return (s - 2) * n * (n - 1) // 2 + n
tri = list(polygon(3, n) for n in range(45, 141))
squ = list(polygon(4, n) for n in range(32, 100))
pent = list(polygon(5, n) for n in range(26, 82))
hexa = list(polygon(6, n) for n in range(23, 71))
hepta = list(polygon(7, n) for n in range(21, 64))
octa = list(polygon(8, n) for n in range(19, 59))

shapes = [tri, squ, pent, hexa, hepta, octa]


def search(n, possible, goal):
    if len(possible) == 0:
        return None
    for i in possible:
        for s in shapes[i]:
            if str(n)[2:] == str(s)[:2]:
                if s == goal:
                    return [(n, i)]
                foo = search(s, list(p for p in possible if not p == i), goal)
                if foo is not None:
                    return [(n, i)] + foo
    return None


seagr = [squ, pent, hexa, hepta, octa]
for i in tri:
    pre = []
    post = []
    for s in seagr:
        for x in s:
            if str(i)[2:] == str(x)[:2]:
                post += [x]
            if str(i)[:2] == str(x)[2:]:
                pre += [x]
    if len(pre) > 0 and len(post) > 0:
        for p in pre:
            foo = search(i, list(asdf for asdf in range(1, 6)), p)
            if foo is not None:
                foo = [(p, 0)]+foo
                if len(foo) == 6:
                    print(foo, sum(a for a, e in foo))
                if len(foo) == 3:
                    print(foo, sum(a for a, e in foo))
#        print(i, prei, posti)
