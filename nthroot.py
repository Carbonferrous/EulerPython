def nthroot(radicand, n):#, base = 10):
    #padding root
    rad = str(radicand)
    if "." not in rad:
        rad += "."
    f = rad.split(".")[0]
    h = rad.split(".")[1]
    f = "0"*((n-len(f))%n) + f
    h = h + "0"*((n-len(h))%n)
    rad = f + h
    #initialization
    #y, r = 0, 0
    b = 10#base
    beta = b - 1
    alpha = int(rad[:n])
    rad = rad[n:] + '0'*n
    #beta = largest beta where (b*y+beta)**n <= temp
    for beta in range(b - 1, -1, -1):
        if beta**n <= alpha:
            break
    yield beta
    y = beta
    r = alpha-beta**n
    #main loop
    while r != 0 or not all(x == '0' for x in rad):
        alpha = int(rad[:n])
        rad = rad[n:] + '0'*n
        temp = b**n*r+alpha + (b*y)**n
        #beta = largest beta where (b*y+beta)**n <= temp
        #(b*y+beta)**n <= temp
        #beta = int(temp ** (1/n) - b*y) + 1
        for beta in range(b - 1, -1, -1):
            if (b*y+beta)**n <= temp:
                break
        yield beta
        r = b**n*r+alpha-(b*y+beta)**n+(b*y)**n
        y = b*y+beta
    for i in range(len(rad)//n-1):
        yield 0
    return

x = nthroot(2, 2)
for i in range(10100):
    print(next(x), end = '')

