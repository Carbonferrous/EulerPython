import numbertheory

def compound(principle, rate, comp, time):
    return principle * pow(1+rate/comp, comp*time)
##a = p(1+r/c)^c*t
##a == p(1 + tr + t(t)/2(r)^2 + ...)
def approx(principle, rate, time):
    x = rate * time
    return principle * (1 + x + x**2/2)

def error(principle, rate, comp, time):
    c = compound(principle, rate, comp, time)
    a = approx(principle, rate, time)
    return (c - a) / c

for p in range(1000, 2000, 1000):
    for r in range(1, 20):
        r = r/100
        for c in [1, 2, 4, 12, 365]:
            for t in range(1, 5):
                if abs(error(p, r, c, t)) > .05: 
                    print(p, r, c, t, error(p, r, c, t))
