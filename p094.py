import numbertheory
#solving ((3*a+-1)/2)**2-3h**2 = 1
#derived from b % 2 == 0 so a**2==h**2+((a+-1)/2)**2
#continued fraction of 3 is 1, 1, 2, 1, 2, ...
##1 + 5 5 6
##2 - 17 17 16
##3 + 65 65 66
##4 - 241 241 240
##5 + 901 901 902
##6 - 3361 3361 3360
##7 + 12545 12545 12546
##8 - 46817 46817 46816
##9 + 174725 174725 174726
##10 - 652081 652081 652080
##11 + 2433601 2433601 2433602
##12 - 9082321 9082321 9082320
##13 + 33895685 33895685 33895686
##14 - 126500417 126500417 126500416
b = [1, 1, 2]
def f(n):
    return numbertheory.contfrac2real([1] + [1,2]*((n-1)//2)+[1]*((n-1)%2))
s = 0
for i in range(4, 31, 2):
    f0, f1 = f(i)
    if f0 % 3 == 1:
        #f0 = (3*a-1)/2, f1 = h, b = a+1
        a = (f0*2+1)//3
        s += 3*a+1
        print(i//2-1, "+", a, a, a+1)
    else:
        #f0 = (3*a+1)/2, f1 = h, b = a-1
        a = (f0*2-1)//3
        s += 3*a-1
        print(i//2-1, "-", a, a, a-1)
    
