def farey(a = 0, b = 1, c = 1, d = 1, x = 1, y = 1, n = 1):
    if b*c - a*d != 1:
        print("Supplied a/b and c/d were not farey neighbours")
        return
    #finds farey neighbour of a,b into c,d
    while b + d <= n:
        c += a
        d += b
    yield (a,b)
    count = 0
    while c/d <= x/y:
        k = int((n+b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        count += 1
        yield (a,b)
    return count - 1
print(list(farey(a = 1, b = 3, c = 1, d = 2, x = 1, y = 2, n = 12)))
