count = 0
for n in range(1,10):
    for x in range(1,25):
        if len(str(n**x))==x:
            count = count + 1
print(count)
