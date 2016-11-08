import math


def D(n):
    if n == 0:
        return 'Fa'
    s = D(n-1)
    r = {'a': 'aRbFR', 'b': 'LFaLb'}
    sn = ''
    for c in s:
        if c in r:
            sn += r[c]
        else:
            sn += c
    return sn.replace('RL', '').replace('LR', '')


def getD(n):
    return D(n).replace('a', '').replace('b', '').replace('F', '')[:-1]


def Ppow2(i):
    c = (0, 1)
    for x in range(i):
        c = (c[0]+c[1], c[1]-c[0])
    return c


def P(n):
    if n == 0:
        return (0, 0)
    if n == 1:
        return (0, 1)
    # floating point error causes problems near 2**i :(
    i = math.ceil(math.log(n, 2))
    assert (2**(i-1) < n and n <= 2**i)
    pn = P(2**i - n)
    c = Ppow2(i-1)
    return (c[0]+c[1]-pn[1], c[1]+pn[0]-c[0])

a = getD(10)
print(P(2**40), Ppow2(40))
