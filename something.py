import math
def isrep(a):
    a = str(a)
    return '' == a.replace(a[0], '')


def rep(a, n):
    return int(str(a)*n)

# nontrivial solutions to rep(a, n) + rep(b, m) = p^2
# 22 + 99 = 121 = 11^2
# 33 + 88 = 121 = 11^2
# 44 + 77 = 121 = 11^2
# 55 + 66 = 121 = 11^2
# 111 + 33 = 144 = 12^2
# 1111 + 333 = 1444 = 38^2
# 44444 + 77 = 44521 = 211^2


for p in range(1, 212):
    p2 = str(p**2)
    m = len(p2)
    for i in range(m-1):
        for j in range(1, 10):
            if isrep(p**2-rep(j, m-i)):
                if len(str(p**2-rep(j, m-i))) > 1:
                    print(rep(j, m-i), '+', p**2-rep(j, m-i), '=', p**2, '=', str(p)+'^2')

# nontrivial solutions to rep(a, n) - rep(b, m) = p^2
# trivial solutions of form:
#   rep(1, 2n+1)-rep(1, 2n) = 10**(2n)
#   rep(4, 2n+1)-rep(4, 2n) = 10**(2n)
#   rep(9, 2n+1)-rep(9, 2n) = 10**(2n)
# 333 - 77 = 256 = 16^2
# 333 - 44 = 289 = 17^2
# 7777 - 888 = 6889 = 83^2
for n in range(2, 5):
    for a in range(1, 10):
        for p in range(1, int(math.sqrt(rep(a, n)))):
            if isrep(rep(a, n) - p**2):
                print(rep(a, n), '-', rep(a, n) - p**2, '=', p**2, '=', str(p)+'^2')
