l = []
for k in range(2, 10):
    for n in range(2, 100):
        l += [(pow(n, k), n, k)]
l.sort()
x = 1
for n, i, k in l:
    if i == sum(map(int, (c for c in str(n)))):
        print(x, n, i, k)
        x += 1
