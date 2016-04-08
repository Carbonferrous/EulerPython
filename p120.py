def r(a, n):
    return ((a - 1) ** n + (a + 1) ** n) % a ** 2
def rmax(a):
    if a % 4 == 0 or a % 4 == 3:
        return r(a, (a - 1)//2)
    if a % 4 == 2:
        return r(a, a-1)
    return r(a, int(a*3/2))
print(sum(rmax(a) for a in range(3, 1001)))
