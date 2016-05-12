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

def pythagTree(limit = None):
    l = limit
    uad = {'u':lambda m, n: (2*m-n, m),
           'a':lambda m, n: (2*m+n, m),
           'd':lambda m, n: (m+2*n, n)}
    root = [(2, 1)]
    branch = []
    if l != None:
        while len(root) > 0:
            for m, n in root:
                yield (m**2-n**2, 2*m*n, m**2+n**2)
                p, q = uad['u'](m, n)
                if p**2+q**2 < l:
                    branch += [(p, q)]
                p, q = uad['a'](m, n)
                if p**2+q**2 < l:
                    branch += [(p, q)]
                p, q = uad['d'](m, n)
                if p**2+q**2 < l:
                    branch += [(p, q)]
            root = branch
            branch = []
        return
    else:
        while True:
            for m, n in root:
                yield (m**2-n**2, 2*m*n, m**2+n**2)
                branch += [uad['u'](m, n)]
                branch += [uad['a'](m, n)]
                branch += [uad['d'](m, n)]
            root = branch
            branch = []
