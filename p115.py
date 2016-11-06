m = 50
a = [1] * m + [2]
n = m + 1
while a[n-1] < 1000000:
    a += [a[n-1] + sum(a[j] for j in range(n-m)) + 1]
    n += 1
print(n-1)
