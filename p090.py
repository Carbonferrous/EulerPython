import itertools
apos = [a for a in itertools.combinations([i for i in range(10)], 6)]
bpos = [b for b in itertools.combinations([i for i in range(10)], 6)]
c = 0
for a in apos:
    for b in apos:
        if not (0 in a and 1 in b or 1 in a and 0 in b):
            continue
        if not (0 in a and 4 in b or 4 in a and 0 in b):
            continue
        if not (0 in a and (6 in b or 9 in b) or (6 in a or 9 in a) and 0 in b):
            continue
        if not (1 in a and (6 in b or 9 in b) or (6 in a or 9 in a) and 1 in b):
            continue
        if not (2 in a and 5 in b or 5 in a and 2 in b):
            continue
        if not (3 in a and (6 in b or 9 in b) or (6 in a or 9 in a) and 3 in b):
            continue
        if not (4 in a and (6 in b or 9 in b) or (6 in a or 9 in a) and 4 in b):
            continue
        if not ((6 in a or 9 in a) and 4 in b or 4 in a and (6 in b or 9 in b)):
            continue
        if not (8 in a and 1 in b or 1 in a and 8 in b):
            continue
        c += 1
print(c//2)
