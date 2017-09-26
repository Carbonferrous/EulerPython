import numbertheory
limit = 120000


def farey(limit):
    n = limit - 1
    a, b, c, d = 0, 1, 1, n
    while c <= n:
        k = int((n+b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        if a + b > limit:
            n = n - 1
            continue
        yield (a, b)
    return


rad = [1]*(limit+1)
for p in numbertheory.primeList(limit):
    rad[p::p] = list(i * p for i in rad[p::p])

s = 0
abchits = []
for a, b in farey(limit):
    c = a + b
    if rad[a]*rad[b]*rad[c] < c:
        abchits += [(a, b, c)]
        s += c

print(s)
