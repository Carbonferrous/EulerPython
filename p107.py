with open('p107_network.txt', 'r') as f:
    M = []
    for x in f.read().split('\n'):
        a = []
        for i in x.split(','):
            if i == '-':
                a += [0]
            else:
                a += [int(i)]
        M += [a]
vertices = [0]
total = sum(sum(i) for i in M)//2
while len(vertices) < 40:
    mw = 0
    mu = 0
    for v in vertices:
        for u, w in enumerate(M[v]):
            if w < mw and u not in vertices and not w == 0 or mw == 0:
                mu = u
                mw = w
    total -= mw
    vertices += [mu]
print(total)
