def polygon(s, n):
    return (s - 2) * n * (n - 1) // 2 + n

def getcyclic(i, p):
    o = []
    for x in p:
        if str(i)[2:] == str(x)[:2] or str(i)[2:][::-1] == str(x)[:2]:
            o += [x]
    return o

tri = []
for n in range(45,140+1):
    tri += [polygon(3, n)]

square = []
for n in range(32,100):
    square += [polygon(4, n)]

penta = []
for n in range(26,82):
    penta += [polygon(5, n)]

hexa = []
for n in range(23,71):
    hexa += [polygon(6, n)]

hepta = []
for n in range(21,64):
    hepta += [polygon(7, n)]

octa = []
for n in range(19,59):
    octa += [polygon(8, n)]

def find(currentshape, searchspace):
    for currentindex in currentshape:
        for nextshape in searchspace:
            if len(nextshape) == 1:
                return nextshape[0]
            possiblenextidexes = getcyclic(currentindex, nextshape)
            if len(possiblenextindexes) == 0:
                continue
            searchspace.remove(nextshape)
            print(find(possiblenextindexes, searchspace))

for i in tri:
	print(i,
              getcyclic(i,square),
              getcyclic(i, penta),
              getcyclic(i, hexa),
              getcyclic(i, hepta),
              getcyclic(i, octa))
