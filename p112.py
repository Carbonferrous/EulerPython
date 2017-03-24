def dec(n, m):
    n = str(n)
    if len(n) == 1:
        return min(int(n), m)
    for a in range(int(n[0])):
        