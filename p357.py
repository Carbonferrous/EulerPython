from numbertheory import divisorList, isPrime, primeList, factor, sqrfree
# 1775261487206
#100
#sqrfree numbers generated 20 considered
#canadite numbers generated 10 considered
#400 10
#1000
#sqrfree numbers generated 204 considered
#canadite numbers generated 35 considered
#8426 27
#10000
#sqrfree numbers generated 2027 considered
#canadite numbers generated 174 considered
#262614 79
#sqrfree numbers generated 20267 considered
#canadite numbers generated 979 considered
#9157936 276
#sqrfree numbers generated 202640 considered
#canadite numbers generated 6329 considered
#524402304 1288
#sqrfree numbers generated 2026416 considered
#canadite numbers generated 44820 considered
#27814470276 6624
#sqrfree numbers generated 20264234 considered
#canadite numbers generated 334924 considered
#1739023853136 39626
#missed n=1, add 1 to above solutions for correct solution
#d+k/d=p
#d**2+k=d*p
#k = d*(p-d)
s = 0
n = 100000000
sqrfr = []
sqrfr = set(list(i for i in sqrfree(n) if i % 2 == 0))
print('sqrfree numbers generated', len(sqrfr), 'considered')
print('yup')
l = []
for pr in primeList(n):
    if pr-1 in sqrfr and isPrime(2+(pr-1)//2):
        l += [pr-1]
print('canadite numbers generated', len(l), 'considered')
c = 0
for i in l:
    t = True
    divisors = list(divisorList(i))
    divisors.sort()
    divisors = divisors[1:]
    for d in divisors:
        if d**2 > i:
            break
        if not isPrime(d+i//d):
            t = False
#            print(i, d, i//d, d+i//d, list(d for d, e in factor(d+i//d)))
            break
    if t:
        s += i
        c += 1
#    if all(isPrime(d+i//d) for d in divisorList(i)):
#        s += i
#        c += 1
#    else:
#        continue
#        print(i, list(d for d, e in factor(i)))
print(s, c)
