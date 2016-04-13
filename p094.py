import numbertheory

def area(a, b, c):
    s = (a + b + c)/2
    return (s*(s-a)*(s-b)*(s-c))**.5

s = 0
for x in range(2, 10**6):
    if area(x, x, x - 1).is_integer():
        s += 3* x - 1
        print(x, x, x - 1, "M")
    if area(x, x, x + 1).is_integer():
        s += 3 * x + 1
        print(x, x, x + 1, "P")
print("Sum:", s)
a = numbertheory.contfracsqrt(3)
b = [next(a), next(a), next(a)]
for x in range(10):
    print(numbertheory.contfrac2real(b))
    b += [b[1]]
    print(numbertheory.contfrac2real(b))
    b += [b[2]]
