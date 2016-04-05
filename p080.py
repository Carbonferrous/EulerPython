import numbertheory

print(sum(sum(int(x) for x in str(numbertheory.stringSqrt(x, 100))) for x in range(1, 101)) - sum(x for x in range(1, 10)) - 1)
