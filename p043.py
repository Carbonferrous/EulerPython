import math
import itertools

a = '0123456789'
b = itertools.permutations(a)
c = [''.join(p) for p in b]
d = list(filter(lambda n: int(n[1:4]) % 2 == 0 and int(n[2:5]) % 3 == 0 and int(n[3:6]) % 5 == 0 and int(n[4:7]) % 7 == 0 and int(n[5:8]) % 11 == 0 and int(n[6:9]) % 13 == 0 and int(n[7:10]) % 17 == 0, c))
print(sum(list(map(int,d))))
