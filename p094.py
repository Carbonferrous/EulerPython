def area(a, b, c):
    s = (a + b + c)/2
    return (s*(s-a)*(s-b)*(s-c))**.5

def isSqr(x):
    est = int(x**.5)
    return est**2 == x

print(area(5,5,6))
