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

p = euler(lambda x, y: 2, (1, 2), .01, [0, 5])
x = list(i for i,j in p)
y = list(j for i,j in p)

plt.plot(x, y)
plt.show()
