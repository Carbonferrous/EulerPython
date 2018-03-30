words = []
sortedwords = {}
with open('p098_words.txt', 'r') as f:
    words = f.read().replace('"', '').split(',')
for w in words:
    sw = ''.join(sorted(w))
    if sw in sortedwords:
        sortedwords[sw] += [w]
    else:
        sortedwords[sw] = [w]
pals = {}
for k in sortedwords:
    if len(sortedwords[k]) > 1:
        if len(sortedwords[k]) > 2:
            print(k, sortedwords[k])
        pals[k] = sortedwords[k]
sq = [i**2 for i in range(4, 31623)]
sortedsq = {}
for s in sq:
    sw = ''.join(sorted(str(s)))
    if sw in sortedsq:
        sortedsq[sw] += [s]
    else:
        sortedsq[sw] = [s]
palss = {}
for k in sortedsq:
    if len(sortedsq[k]) > 1:
        palss[k] = sortedsq[k]
print(pals)