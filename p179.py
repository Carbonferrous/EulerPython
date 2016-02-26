import numbertheory
divcount = list(numbertheory.numDivisorList(10**7))
count = 0
for a in range(2, 10**7 - 1):
    if divcount[a] == divcount[a+1]:
        count += 1
print(count)
