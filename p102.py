def contains0(points):
    v = [0, 0]
    v0 = points[0]
    v1 = [points[1][0] - v0[0], points[1][1] - v0[1]]
    v2 = [points[2][0] - v0[0], points[2][1] - v0[1]]
    a = (det(v, v2) - det(v0, v2))/det(v1, v2)
    b = -(det(v, v1) - det(v0, v1))/det(v1, v2)
    if a > 0 and b > 0 and a + b < 1:
        return 1
    return 0
def det(u, v):
    return u[0]*v[1] - u[1]*v[0]
f = open("p102_triangles.txt", 'r')
s = 0
for x in range(1000):
    l = f.readline().split(',')
    l[5] = l[5][:-1]
    a = [(int(l[0]), int(l[1])),(int(l[2]), int(l[3])),(int(l[4]), int(l[5]))]
    s += contains0(a)
print(s)
