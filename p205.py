from combinatorics import polynomial

p = polynomial()
p += {1: 1, 2: 1, 3: 1, 4: 1}
p = p**9
pt = p.evaluate(1)

c = polynomial()
c += {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
c = c**6
ct = c.evaluate(1)

print(p, pt)
print(c, ct)
s = 0
for k in p:
    cs = sum(c[a] for a in c if a < k)
    s += p[k]*cs
s = s/pt/ct
print(round(s, 7))