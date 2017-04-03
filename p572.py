def test(M):
    r1, r2, r3 = M
    a, b, c = r1
    d, e, f = r2
    g, h, i = r3

    x = a**2+b*d+c*g == a and a*b+b*e+c*h == b and a*c+b*f+c*i == c
    y = a*d+d*e+f*g == d and b*d+e**2+f*h == e and c*d+e*f+f*i == f
    z = a*g+d*h+g*i == g and b*g+e*h+h*i == h and c*g+f*h+i**2 == i
    return x and y and z
n = 1
count = 0
for a in range(-n, n+1):
    for b in range(-n, n+1):
        for c in range(-n, n+1):
            for d in range(-n, n+1):
                for e in range(-n, n+1):
                    for f in range(-n, n+1):
                        for g in range(-n, n+1):
                            for h in range(-n, n+1):
                                for i in range(-n, n+1):
                                    M = [[a, b, c], [d, e, f], [g, h, i]]
                                    if test(M):
#                                       print(M)
                                        count += 1
print(count)
