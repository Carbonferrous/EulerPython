import numbertheory, itertools

print(sum(sum(itertools.islice(numbertheory.sqrtGen(x),100))) for x in range(1, 101)) - sum(x for x in range(1, 10)) - 1)
