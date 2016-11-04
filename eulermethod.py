import math, scipy
import numpy as np
import matplotlib.pyplot as plt

def euler(dydx, init, step, xrange, maxstep = 1000):
    points = [init]
    x, y = init
    m = dydx(*init)
    while x+step <= xrange[1] and len(points) <= maxstep:
        x = x+step
        y = y+m*step
        points += [(x, y)]
        m = dydx(x, y)
    x,y = init
    m = dydx(*init)
    while x-step >= xrange[0] and len(points) <= maxstep:
        x = x-step
        y = y-m*step
        points = [(x, y)]+points
        m = dydx(x, y)
    return points

p = euler(lambda x, y: 7*x**2-x**2*y, (0, 2), .4, [0, 1.3])
x = list(i for i,j in p)
y = list(j for i,j in p)
print(p)
plt.plot(x, y)
plt.show()
