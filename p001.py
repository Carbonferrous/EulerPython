def sumdivisibleby(x, d):
    return d*int(x/d)*(1+int(x/d))//2
x = 1000-1
print(sumdivisibleby(x, 3) + sumdivisibleby(x, 5) - sumdivisibleby(x, 15))
