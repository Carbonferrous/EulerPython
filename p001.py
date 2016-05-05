def s(x, d):
    return d*int(x/d)*(1+int(x/d))//2
x = 999
print(s(x, 3) + s(x, 5) - s(x, 15))
