import fractions
p = 1
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                f = fractions.Fraction(10*a+b, 10*c+d)
                w = fractions.Fraction(a,c)
                x = fractions.Fraction(a,d)
                y = fractions.Fraction(b,c)
                z = fractions.Fraction(b,d)
                if f>=1:
                    pass
                elif (f==w and b==d) or (f==x and b==c) or (f==y and a==d) or (f==z and a==c):
                    print(10*a+b, 10*c+d, f)
                    p *= f
print(p)
