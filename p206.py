def combine(n):
    l = [x for x in n]
    s = ''
    for i, x in enumerate(l):
        s += str(i + 1)+str(x)
    return int(s+'0')


def isform(n):
    n = str(n)
    return all((n[2*i] == str((i+1) % 10)) for i in range(10))

# 1389019170 1929374254627488900
for n in range(1010101070, 1389026670+1, 100):
    if isform(n**2):
        print(n, n**2)
        break
