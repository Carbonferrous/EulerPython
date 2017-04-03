M = {'D': lambda a: a//3, 'U': lambda a: (4*a+2)//3, 'd': lambda a: (2*a-1)//3}
Mp = {'D': lambda a: a*3, 'U': lambda a: (3*a-2)//4, 'd': lambda a: (3*a+1)//2}


def mcollatz(n, c=-1):
    s = ''
    while not c == 0 and not n == 1:
        if n % 3 == 0:
            n = M['D'](n)
            s += 'D'
        elif n % 3 == 1:
            n = M['U'](n)
            s += 'U'
        elif n % 3 == 2:
            n = M['d'](n)
            s += 'd'
        c -= 1
    return s, n


def rmcollatz(s, n=0):
    s = s[::-1]
    for c in s:
        n = Mp[c](n)
    return n


s = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'


def basis(s):
    key = {'D': 0, 'U': 1, 'd': 2}
    base = [[(1, 3), (2, 6), (0, 9)],
            [(0, 4), (1, 7), (2, 10)],
            [(1, 2), (2, 5), (0, 8)]]
    base = base[key[s[0]]]
    base.sort()
    base = list(j for asdf, j in base)
    i = 2
    for c in s[1:]:
        b = base[key[c]]
        for j in range(3):
            m, k = mcollatz(b+j*3**i, i)
            base[k % 3] = b+j*3**i
        i += 1
    return base
b = basis(s)
m = min(b)
m = m + ((10**15-m)//3**len(s)+1)*3**len(s)
while m < 10**15:
    m += 3**len(s)
print(m)
