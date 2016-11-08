cardvalue = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8,
             'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}


def royalflush(c):
    suit = list(c)[0][1]
    # make sure all suits are the same
    if not all(i[1] == suit for i in c):
        return False
    values = set(i[0] for i in c)
    return all(i in values for i in range(9, 14))


def straightflush(c):
    suit = list(c)[0][1]
    # make sure all suits are the same
    if not all(i[1] == suit for i in c):
        return 0
    values = sorted(list(i[0] for i in c))
    if not values == list(range(values[0], values[-1]+1)):
        return 0
    return values[0]


def fourofakind(c):
    values = sorted(list(i[0] for i in c))
    if len(set(values)) != 2:
        return 0
    if values[2] == values[1] and values[2] == values[3]:
        return values[2]
    return 0


def fullhouse(c):
    values = sorted(list(i[0] for i in c))
    if len(set(values)) != 2:
        return 0
    if values[2] == values[1] or values[2] == values[3]:
        return values[2]
    return 0


def flush(c):
    suit = list(c)[0][1]
    if all(i[1] == suit for i in c):
        return highcard(c)
    return 0


def straight(c):
    values = sorted(list(i[0] for i in c))
    if not values == list(range(values[0], values[-1]+1)):
        return 0
    return values[0]


def threeofakind(c):
    values = list(i[0] for i in c)
    for i in range(1, 14):
        if values.count(i) == 3:
            return i
    return 0


def twopairs(c):
    values = list(i[0] for i in c)
    x = 0
    for i in range(1, 14):
        if values.count(i) == 2:
            x += 1
        if x == 2:
            return i
    return 0


def onepair(c):
    values = list(i[0] for i in c)
    for i in range(1, 14):
        if values.count(i) == 2:
            return i
    return 0


def highcard(c):
    return max(g[0] for g in c)


def score(c):
    if royalflush(c):
        #        print('Royal Flush!', c)
        return (9, 1)
    if straightflush(c) != 0:
        #        print('Straight Flush!', c, straightflush(c))
        return (8, straightflush(c))
    if fourofakind(c) != 0:
        #        print('Four of a Kind!', c, fourofakind(c))
        return (7, fourofakind(c))
    if fullhouse(c) != 0:
        #        print('Full House!', c, fullhouse(c))
        return (6, fullhouse(c))
    if flush(c) != 0:
        #        print('Flush!', c, flush(c))
        return (5, flush(c))
    if straight(c) != 0:
        #        print('Straight!', c, straight(c))
        return (4, straight(c))
    if threeofakind(c) != 0:
        #        print('Three of a Kind!', c, threeofakind(c))
        return (3, threeofakind(c))
    if twopairs(c) != 0:
        #        print('Two Pairs!', c, twopairs(c))
        return (2, twopairs(c))
    if onepair(c) != 0:
        #        print('One Pair!', c, onepair(c))
        return (1, onepair(c))
    return (0, highcard(c))


f = open('p054_poker.txt', 'r')
count1 = 0
count2 = 0
i = 0
for l in f:
    i += 1
    c = l.strip().split(' ')
    p1, p2 = c[:5], c[5:]
    p1 = set([(cardvalue[a[0]], a[1]) for a in p1])
    p2 = set([(cardvalue[a[0]], a[1]) for a in p2])
    s1 = score(p1)
    s2 = score(p2)
    if s1 == s2:
        s1 = highcard(p1)
        s2 = highcard(p2)
    if s1 > s2:
        count1 += 1
    elif s2 > s1:
        count2 += 1
    else:
        raise Exception('scores were the same?', p1, p2, s1, s2)
print(count1)
