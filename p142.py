##x+y
##x-y
##x+z
##x-z
##y+z
##y-z

def f(x, y, z):
    return (x+y, x-y, x+z, x-z, y+z, y-z)
#key is center between two squares, data is how far apart they are
s = {}
for i in range(1, 1000):
    for x in range(2, 2*1000+1,2):
        c = ((i+x)**2+i**2)//2
        if c in s:
            s[c] += [c-i**2]
        else:
            s[c] = [c-i**2]
for c in s:
    if len(s[c]) < 2:
        continue
    for d in s[c]:
        if d in s:
            #print(c, s[c], d, s[d])
            for e in s[d]:
                if e in s[c]:
                    print(c, d, e)
                    print(c+d+e)
                    print(f(c, d, e))
