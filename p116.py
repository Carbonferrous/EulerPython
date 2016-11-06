# r_n = r_{n-1} + r_{n-2} + 1
# g_n = g_{n-1} + g_{n-3} + 1
# b_n = b_{n-1} + b_{n-4} + 1
r = [0]*2 + [1]
g = [0]*3 + [1]
b = [0]*4 + [1]
for n in range(2+1, 50+1):
    r += [r[n-1] + r[n-2] + 1]
for n in range(3+1, 50+1):
    g += [g[n-1] + g[n-3] + 1]
for n in range(4+1, 50+1):
    b += [b[n-1] + b[n-4] + 1]
print(r[50]+g[50]+b[50])
