def fibList(UpperLimit):
    a, b, c = 1, 1, 2
    fib = [a, b]
    while c < UpperLimit:
        fib.append(c)
        a, b = b, c
        c = a + b
    return fib

print(sum(filter(lambda x: x % 2 == 0, fibList(4000000))))
