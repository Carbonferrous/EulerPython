from combinatorics import fib, _fib
import math
def n(fibonacciTerm):
    return int(round(math.log(10, (1+math.sqrt(5))/2) * (math.log(fibonacciTerm, 10) + math.log(math.sqrt(5), 10)),0)+.5)
