# a_n = a_{n-1} + a_{n-2} + a_{n-3} + a_{n-4}
a = [1, 1, 2, 4]
for n in range(4, 50+1):
    a += [a[n-1]+a[n-2]+a[n-3]+a[n-4]]
print(a[50])
