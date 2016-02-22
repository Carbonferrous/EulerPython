import math
def box(numBox, maxInBox, chips):
    if numBox <= 0 or maxInBox <= 0 or chips <= 0 or numBox*maxInBox < chips:
        return 0
    if numBox*maxInBox == chips:
        return 1
    if chips <= maxInBox:
        return nCr(chips + numBox - 1,chips)
    s = 0
    for a in range(0, 1 + maxInBox):
        s += box(numBox - 1, maxInBox, chips - a)
    return s
def nCr(n, r):
    return math.factorial(n)//math.factorial(r)//math.factorial(n-r)
print(box(500,5,20))
