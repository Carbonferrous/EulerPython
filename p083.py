with open("p083_matrix.txt") as fileInput:
    M = [[int(i) for i in x.split(',')] for x in fileInput.read().split("\n")]

q = list((i, j) for j in range(80) for i in range(80))
d = dict(((i, j), 32078320) for j in range(80) for i in range(80))
p = dict(((i, j), (0, 0)) for j in range(80) for i in range(80))
d[(0, 0)] = M[0][0]

while len(q) > 0:
    m = d[q[0]]
    mu = q[0]
    for u in q:
        if d[u] < m:
            m = d[u]
            mu = u
    q.remove(mu)
    try:
        v = (mu[0]+1, mu[1])
        alt = d[mu]+M[v[0]][v[1]]
        if alt < d[v]:
            d[v] = alt
            p[v] = mu
    except (IndexError, KeyError):
        pass
    try:
        v = (mu[0]-1, mu[1])
        alt = d[mu]+M[v[0]][v[1]]
        if alt < d[v]:
            d[v] = alt
            p[v] = mu
    except (IndexError, KeyError):
        pass
    try:
        v = (mu[0], mu[1]+1)
        alt = d[mu]+M[v[0]][v[1]]
        if alt < d[v]:
            d[v] = alt
            p[v] = mu
    except (IndexError, KeyError):
        pass
    try:
        v = (mu[0], mu[1]-1)
        alt = d[mu]+M[v[0]][v[1]]
        if alt < d[v]:
            d[v] = alt
            p[v] = mu
    except (IndexError, KeyError):
        pass
print(d[(79, 79)])
