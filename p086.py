def pythagTreeTraverse(traversal):
    uad = {'u':lambda m, n: (2*m-n, m),
           'a':lambda m, n: (2*m+n, m),
           'd':lambda m, n: (m+2*n, n)}
    uad['U'] = uad['u']
    uad['A'] = uad['a']
    uad['D'] = uad['d']
    m, n = 2, 1
    for t in traversal:
        m, n = uad[t](m, n)
    return (m**2-n**2, 2*m*n, m**2+n**2)

def pythag(limits = lambda m,n: True):
    #a, b, c = m**2-n**2, 2*m*n, m**2+n**2
    uad = {'u':lambda m, n: (2*m-n, m), #increases at rate approaching 1 (smaller than d)
           'a':lambda m, n: (2*m+n, m), #increases at rate approaching 2sqrt2+3
           'd':lambda m, n: (m+2*n, n)} #increases at rate approaching 1
    l = limits #function of m,n to define when to continue
    root = [(2, 1)]
    branch = []
    while len(root) > 0:
        for m, n in root:
            yield (m**2-n**2, 2*m*n, m**2+n**2)
            p, q = uad['u'](m, n)
            if l(p, q):
                branch += [(p, q)]
            p, q = uad['d'](m, n)
            if l(p, q):
                branch += [(p, q)]
            p, q = uad['a'](m, n)
            if l(p, q):
                branch += [(p, q)]
        root = branch
        branch = []
