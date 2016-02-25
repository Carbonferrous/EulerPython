divcount = [1]*10**7
for n in range(2, 10**7):
    for x in range(n, 10**7, n):
        divcount[x] += 1
count = 0
for a in range(2, 10**7 - 1):
    if divcount[a] == divcount[a+1]:
        count += 1
print(count)
