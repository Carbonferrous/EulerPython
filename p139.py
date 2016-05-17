def sol(p):
    count = 0
    a, b, c = 3, 4, 5
    i = 0
    while a+b+c < p:
        count += (p-1)//(a+b+c)
        i += 1
        a, b, c = a+2*b+2*c, 2*a+b+2*c, 2*a+2*b+3*c
    return count

print(sol(10**8))
