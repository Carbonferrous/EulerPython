import itertools

def pentaList():
    x = 1
    while True:
        yield x*(3*x-1)//2
        x += 1

foo = False
pL = list(itertools.islice(pentaList(), 10000))
for a in pL:
    for b in pL:
        if (a+b) in pL and abs(a - b) in pL:
            print(a, b, abs(a - b))
            foo = True
            break
    if foo:
        break
