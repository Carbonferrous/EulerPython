import numbertheory
num = 10
while True:
    a = [div for div, exp in numbertheory.primeFactor(num)]
    b = [div for div, exp in numbertheory.primeFactor(num+1)]
    c = [div for div, exp in numbertheory.primeFactor(num+2)]
    d = [div for div, exp in numbertheory.primeFactor(num+3)]
    if len(a) == 4 and len(b) == 4 and len(c) == 4 and len(d) == 4:
        print(num)
        break
    num += 1
