import itertools

WIN = 1
LOSE = -1

results = dict()

matches = 20

def match(a, b, result):
    pair = (a, b) if (a < b) else (b, a)
    res = result if (a < b) else -result
    if pair not in results:
        results[pair] = result
    else:
        assert results[pair] == res

teams = list(range(matches + 1))

for i in teams:
    for j in range(matches // 2):
        o = (i + j + 1) % len(teams)
        print(i, "wins against", o)
        match(i, o, WIN)
    for j in range(matches // 2, matches):
        o = (i + j + 1) % len(teams)
        print(i, "loses against", o)
        match(i, o, LOSE)

wins = [0] * (matches + 1)
losses = [0] * (matches + 1)
for k, v in results.items():
    winner = k[0] if v == WIN else k[1]
    loser = k[1] if v == WIN else k[0]
    wins[winner] += 1
    losses[loser] += 1

print(wins, losses)

print(sum(1 for _ in filter(lambda a: a, itertools.starmap(lambda a, b, c: results[(a, b)] == WIN and results[(b, c)] == WIN and results[(a, c)] == LOSE, itertools.combinations(teams, 3)))))
