import numbertheory
import math
import numpy as np


def row(n):
    return (n-1)*n//2+1, n*(n+1)//2


# find centers
def find_center(r, ls, lssiv, n):
    centers = []
    a, b = row(r)
    lsra = np.where(np.logical_and(row(r-1)[0] <= ls, ls <= row(r+1)[1]))[0]
    lsr = ls[lsra[0]:lsra[-1]+1]
    for p in lsr:
        tp = [p]
        c = 1
        if a < p and p < b-1:
            if lssiv[p+r-n] == 1:
                c += 1
                tp += [p+r]
            if lssiv[p+r+1-n] == 1:
                c += 1
                tp += [p+r+1]
            if lssiv[p+r-1-n] == 1:
                c += 1
                tp += [p+r-1]
            if lssiv[p-r-n] == 1:
                c += 1
                tp += [p-r]
            if lssiv[p-r+1-n] == 1:
                c += 1
                tp += [p-r+1]
            if lssiv[p-r+2-n] == 1:
                c += 1
                tp += [p-r+2]
            if c >= 3:
                centers += tp
        elif p == a:
            if lssiv[p+r-n] == 1:
                c += 1
                tp += [p+r]
            if lssiv[p+r+1-n] == 1:
                c += 1
                tp += [p+r+1]
            if lssiv[p-r+1-n] == 1:
                c += 1
                tp += [p-r+1]
            if lssiv[p-r+2-n] == 1:
                c += 1
                tp += [p-r+2]
            if c >= 3:
                centers += tp
    return centers
def solution(r):
    # generate primes 2 rows away from the search row
    n = row(r-2)[0]
    m = row(r+2)[1]
    ls, lssiv = numbertheory.primeListRange(n,m)
    ls = np.array(ls)
    centers = find_center(r-1, ls, lssiv, n)
    centers += find_center(r, ls, lssiv, n)
    centers += find_center(r+1, ls, lssiv, n)
    centers = list(set(centers))
    tprime_found = []
    a, b = row(r)
    for i in centers:
        if i < a or i > b or i in tprime_found:
            continue
        tprime_found += [i]
    return sum(tprime_found)
print(solution(10000))
print(solution(5678027)+solution(7208785))
# 5678027 has 79697256800321526 sol
# 7208785 has 242605983970758409 sol
# 322303240771079935 total sol