# f(0)=0
# f(1)=1
# f(2)=2 : 1+1=2
# f(3)=1 : 1+2
# f(4)=3 : 4=2+2=2+1+1
# f(5)=2 : 4+1=2+2+1
# f(6)=3 : 4+2=4+1+1=2+2+1+1
# f(7)=1 : 4+2+1
# f(8)=4 : 8=4+4=4+2+2=4+2+1+1
# f(9)=3 : 8+1=4+4+1=4+2+2+1

# a   b
# 11110000001XXX p
# 111100000002XX q
# 1110200000XXXX
# 1102200000XXXX
# 1022200000XXXX
# p = p+q+(a-1)*(b*(p+q)+q)
# q = b*(p+q)+q
import re


def f(n):
    s = '{:b}'.format(n)
    t = re.split('(1+0+)', s)
    t = list(i for i in t if not i == '')
    p = 1
    q = 0
    for c in t[::-1]:
        a = c.count('1')
        b = c.count('0')
        p, q = p+q+(a-1)*(b*(p+q)+q), b*(p+q)+q
    su = p+q
    return su

print(f(10**25))
