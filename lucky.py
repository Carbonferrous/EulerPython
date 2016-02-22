def lucky(n):
    yield 1
    siv = list(range(1,n))
    temp = siv
    a = 1
    d = 2
    while a < len(siv):
        temp = list(filter(lambda x: (x[0]+1) % d != 0, list(enumerate(siv))))
        siv = list(temp[n][1] for n in range(0,len(temp)))
        d = siv[a]
        yield siv[a]
        a += 1
