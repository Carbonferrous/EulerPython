from combinatorics import fib
def superfib(a_, A, b_, B, n):
    Fn = fib(b_ - a_)
    G1 = (fib(2-a_)*B - (-1)**(b_-a_)*fib(2-b_)*A)/Fn
    G2 = (fib(n+2-a_)*B - (-1)**(b_-a_)*fib(n+2-b_)*A)/Fn
    return G2 - G1 - A - B


## Test Case 1
## 1 2 3 4 5 6 7  8  9  10 11
## 1 1 2 3 5 8 13 21 34 55 89
print(superfib(1, 1, 2, 1, 7))

## Test Case 1
## 1 2 3  4  5  6  7  
## 7 5 12 17 29 46 75 
print(superfib(1, 7, 2, 5, 5))
