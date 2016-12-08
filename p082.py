import copy
with open("p081_matrix.txt") as fileInput:
    M = [[int(i) for i in x.split(',')] for x in fileInput.read().split("\n")]
T = copy.deepcopy(M)

for c in range(1, len(M[0])):
    for r in range(len(M)):
        m = T[r][c-1]
        for i in range(r):
            mtemp = sum(M[j][c] for j in range(i, r))+T[i][c-1]
            if mtemp < m:
                m = mtemp
        for i in range(r+1, len(M)):
            mtemp = sum(M[j][c] for j in range(r+1, i+1))+T[i][c-1]
            if mtemp < m:
                m = mtemp
        T[r][c] = M[r][c] + m
print(min(r[-1] for r in T))
