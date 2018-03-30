s = list(((100003 - 200003*k + 300007*k**3) % 1000000) - 500000 for k in range(1, 56))
for k in range(56, 4000000 + 1):
    s += [((s[k-24 - 1] + s[k-55 - 1]) % 1000000) - 500000]
print(s[9], s[99])
m = list(list(s[j+2000*i] for j in range(2000)) for i in range(2000))
def maxsub(m):
    ms = 0
    for i in range(len(m)):
        j = [0]
        for k in range(len(m[i])):
            j += [j[-1] + m[i][k]]
        if j.index(min(j)) < j.index(max(j)):
            msi = max(j) - min(j)
        else:
            if max(j[j.index(min(j)):]) - min(j) > max(j) - min(j[:j.index(max(j))]+[-500000]):
                msi = max(j[j.index(min(j)):]) - min(j)
            else:
                msi = max(j) - min(j[:j.index(max(j))]+[-500000])
        if msi > ms:
            ms = msi
    return ms
cont = []
cont += [maxsub(m)]
print(cont)
mv = list(list(m[r][c] for r in range(len(m))) for c in range(len(m[0])))
cont += [maxsub(mv)]
print(cont)
atd = list(list(m[r][r+d] for r in range(len(m)) if r+d >= 0 and r >= 0 and r < len(m) and r+d < len(m)) for d in range(-len(m)+1, len(m)))
cont += [maxsub(atd)]
print(cont)
diag = list(list(mv[r][r+d] for r in range(len(mv)) if r+d >= 0 and r >= 0 and r < len(mv) and r+d < len(mv)) for d in range(-len(mv)+1, len(mv)))
cont += [maxsub(diag)]
print(cont)
print(max(cont))