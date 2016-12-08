import copy


def possible(M, i, j):
    if not M[i][j] == 0:
        return []
    l = list(range(1, 10))
    for e in M[i]:
        try:
            l.remove(e)
        except ValueError:
            pass
    for k in range(9):
        try:
            l.remove(M[k][j])
        except ValueError:
            pass
    for x in range((i//3)*3, (i//3)*3+3):
        for y in range((j//3)*3, (j//3)*3+3):
            try:
                l.remove(M[x][y])
            except ValueError:
                pass
    return l


def sudokusolver(O):
    M = copy.deepcopy(O)
    # solves by deduction
    flag = True
    while flag:
        flag = False
        for nx in range(9):
            for ny in range(9):
                l = possible(M, nx, ny)
                if len(l) == 1:
                    M[nx][ny] = l[0]
                    flag = True
                if len(l) == 0 and M[nx][ny] == 0:
                    raise Exception('unsolveable?')
    return M

# start with nx = 0, ny = 0
# if M[nx][ny] == 0:
#    if no possible:
#        return M
#    for each possible:
#        A = solve(m)
#        if A contains 0's
#            continue
#        else:
#            return M
# else:
#    move to next index
#    solve(M)


def nextindex(nx, ny):
    if nx < 9:
        nx += 1
        if nx == 9:
            nx = 0
            ny += 1
            if ny == 9:
                ny = 0
    return nx, ny


def solve(S, nx=0, ny=0):
    M = copy.deepcopy(S)
    if M[nx][ny] == 0:
        p = possible(M, nx, ny)
        if len(p) == 0:
            return M
        else:
            for i in p:
                M[nx][ny] = i
                A = solve(M, *nextindex(nx, ny))
                if any(0 in r for r in A):
                    continue
                else:
                    break
            return A
    else:
        if nx < 9:
            nx += 1
            if nx == 9:
                nx = 0
                ny += 1
                if ny == 9:
                    return M
        return solve(M, nx, ny)

f = open('p096_sudoku.txt', 'r')
s = 0
for i in range(50):
    M = []
    print(f.readline().strip())
    for j in range(9):
        M += [list(map(int, list(f.readline().strip())))]
    print(M)
    M = sudokusolver(M)
    S = solve(M)
    print(S)
    s += int(''.join(map(str, S[0][:3])))
print(s)
