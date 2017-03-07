import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
path = 'C:\\Users\\Dalsnuten\\Desktop\\stuff\\'

# reflects the line from m1, m2 to x, y at the point x, y
def reflect(x, y, m1, m2):
    assert abs(4*x**2 + y**2 - 100) < 0.0001
    theta = math.atan2(-y, -4*x)
    beta = math.atan2(m2-y, m1-x)
    return math.tan(2*theta-beta)


# travlels along line to next point
def travel(x, y, m):
    x1 = -(2*math.sqrt(-m**2*(x**2-25)+2*m*x*y-y**2+100)-m*(m*x-y))/(m**2+4)
    y1 = -2*(m*math.sqrt(-m**2*(x**2-25)+2*m*x*y-y**2+100)+2*(m*x-y))/(m**2+4)
    x2 = (2*math.sqrt(-m**2*(x**2-25)+2*m*x*y-y**2+100)+m*(m*x-y))/(m**2+4)
    y2 = 2*(m*math.sqrt(-m**2*(x**2-25)+2*m*x*y-y**2+100)-2*(m*x-y))/(m**2+4)
    d1 = math.sqrt((x-x1)**2 + (y-y1)**2)
    d2 = math.sqrt((x-x2)**2 + (y-y2)**2)
    if d1 > d2:
        return (x1, y1)
    return (x2, y2)


# tests whether reached opening
def test(x, y):
    if abs(x) <= 0.01 and y > 0:
        return False
    return True

#initiate plot
ellipse = Ellipse(xy=(0, 0), width=10, height=20)
fig, ax = plt.subplots()
ax.add_patch(ellipse)
ellipse.set_alpha(.7)
ellipse.set_facecolor((0, 0, 0))
ax.set_aspect('equal')
plt.axis([-5, 5, -10, 10])
plt.axis('off')
# initiate positions
count = 0
m = (10.1-(-9.6))/(0-1.4)
x1, y1 = 0, 10.1
x2, y2 = travel(x1, y1, m)
m = reflect(x2, y2, x1, y1)

# plot line
plt.plot((x1, x2), (y1, y2), color='r')
plt.savefig(path+'0.png', bbox_inches='tight')

while test(x2, y2):
    # move to next point
    count += 1
    x1, y1 = x2, y2
    x2, y2 = travel(x1, y1, m)
    m = reflect(x2, y2, x1, y1)
    # plot line
    plt.plot((x1, x2), (y1, y2), color='r')
    plt.savefig(path+str(count)+'.png', bbox_inches='tight')
print(count)

plt.show()
