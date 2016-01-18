count = 0
for x in range(1,10001):
    test = x
    lychrelNumber = True
    for i in range(0,50):
        if(test + int(str(test)[::-1]) == int(str(test + int(str(test)[::-1]))[::-1])):
            lychrelNumber = False
            break
        else:
            test = int(test + int(str(test)[::-1]))
    if(lychrelNumber):
        print(x)
        count = count + 1
print(count)
