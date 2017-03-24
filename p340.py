# So much induction ...
# So basically if you print F(n, a, b, c), notice that it increments by 1 and
# then drops by some amount repeatedly
# After playing around with the drops and other stuff, a summation formula was
# derived and condensed to just variables. it can probably be simplified, but
# effort


def F(n, a, b, c):
    if n > b:
        return n - c
    return F(a + F(a + F(a + F(a + n, a, b, c), a, b, c), a, b, c), a, b, c)


def f(n, a, b, c):
    d = -4*a+3*c+1  # jump
    fb = 4*b-3*(b % a)-4*c-3*c*((b//a)-1)+1  # (b%a)+1 term
    i = (n-(b % a)-1)//a  # nearest drop index
    # base term + increments and drop to nearest drop index and incremented
    fi = fb + i*(a-1+d)+n-((b % a)+1+i*a)
    return fi


# condensed form of f(n, a, b, c)
def g(n, a, b, c):
    fi = 4*b - c - 4*(b % a) - 3*c*(b//a) + (-4*a + 3*c)*((n-(b % a)-1)//a) + n
    return fi


# basic sum formula for testing
def S1(a, b, c):
    return sum(F(n, a, b, c) for n in range(b+1))


# simplified sum formula from g(n, a, b, c) and other testing
def S(a, b, c):
    total = (4*b - c - 4*(b % a) - 3*c*(b//a))*(b+1) + (b)*(b+1)//2
    i = (b-(b % a)-1)//a
    total += (-4*a + 3*c)*(a*i*(i+1)//2-(b % a)-1)
    return total
# a > c
a = 21**7
b = 7**21
c = 12**7
# for i in range(b + 1):
#    if not(F(i, a, b, c) == f(i, a, b, c) and f(i, a, b, c) == g(i, a, b, c)):
#        print(i, F(i, a, b, c), f(i, a, b, c), g(i, a, b, c))
# print(S(a, b, c), S1(a, b, c))
print(S(a, b, c) % 10**9)
# #drop on the (b % a) + 1 + n*a index for n = ..., -1, 0, 1, 2, 3, ...
# print('predicting drop indexes', a, b, c)
# for n in range(2):
#    print((b % a) + 1 + n*a)
# #magnitude of drop is 4*a-3*c-1
# print('predicting magnitude of drop', a, b, c)
# for c in range(a):
#    print(c, F(b % a)-F((b % a) + 1), a*4-1-3*c)
# #value of index at drop f((b%a)+1) -3*(b%a)
# print('testing first term or something', a, b, c)
# for a in range(max(1,c), b+1):
#    print(a, b%a, F((b % a) + 1), 4*b-3*(b%a)-4*c-3*c*((b//a) - 1)+1)
