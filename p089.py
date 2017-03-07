with open('p089_roman.txt', 'r') as f:
    romantest = f.read().strip().split('\n')


def greedy(n):
    g = [(1000, 'M'),
         (900, 'CM'),
         (500, 'D'),
         (400, 'CD'),
         (100, 'C'),
         (90, 'XC'),
         (50, 'L'),
         (40, 'XL'),
         (10, 'X'),
         (9, 'IX'),
         (5, 'V'),
         (4, 'IV'),
         (1, 'I')]
    roman = ''
    while not n == 0:
        for a, b in g:
            if n >= a:
                roman += b
                n -= a
                break
    return roman


def rton(roman):
    inte = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    order = 'MDCLXVI'
    s = inte[roman[-1]]
    for i in range(len(roman)-1):
        if order.index(roman[i]) > order.index(roman[i+1]):
            s -= inte[roman[i]]
        else:
            s += inte[roman[i]]
    return s

initial = sum(len(i) for i in romantest)
romantest = list(map(rton, (i for i in romantest)))
romantest = list(map(greedy, (i for i in romantest)))
final = sum(len(i) for i in romantest)
print(initial-final)
