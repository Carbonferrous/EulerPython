def cubeperm(n):
    n = n**3
    n = str(n)
    n = list(str(i) for i in n)
    n = sorted(n)
    n = ''.join(i for i in n)
    return n
t = {}
limit = 10000
for c in range(limit):
    t[cubeperm(c)] = 0
for c in range(limit):
    t[cubeperm(c)] += 1

key = [key for key, value in t.items() if value == 5]

for c in range(limit):
    if cubeperm(c) in key:
        key.remove(cubeperm(c))
        print(c**3, cubeperm(c))
