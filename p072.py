from numbertheory import totient
s = 0
for x in range(2, 1000000 + 1):
    s += totient(x)
print(s)
