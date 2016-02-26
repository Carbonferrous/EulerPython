s = 0
for x in range(1,1000001):
    x = str(x)
    if x == x[::-1]:
        x = "{0:b}".format(int(x))
        if x == x[::-1]:
            s += int(x,2)
print(s)
