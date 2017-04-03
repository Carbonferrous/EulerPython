n = 1000000
m = [0]*n

for i in range(2, n):
    m[i] = max(m[i], i - int((i-1)/9)*9)
    m[i::i] = list(max(k, m[i]+m[j]) for j, k in enumerate(m[i::i], 1))
print(sum(m))