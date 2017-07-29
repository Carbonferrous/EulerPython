# doesn't really take into account go to jail after 2 doubles in a row, but whatever
from numpy import linalg
import numpy as np
# first number is how often doubles get sent to jail,
# also includes doubles not counted
baseroll = [1/12, 0, 0, 1/16-1/48, 1/8, 3/16-1/48, 1/4, 3/16-1/48, 1/8, 1/16-1/48]
baseroll = [0, 0, 0, 1/16, 1/8, 3/16, 1/4, 3/16, 1/8, 1/16]
#baseroll = [2/36, 0, 0, 1/36-1/108, 2/36, 3/36-1/108, 4/36, 5/36-1/108, 6/36, 5/36-1/108, 4/36, 3/36-1/108, 2/36, 1/36-1/108]
#baseroll = [0, 0, 0, 1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
# making initial transition matrix 
transition = [[0 for j in range(40)] for i in range(40)]
for i in range(40):
    for j in range(len(baseroll)-1):
        transition[i][(i+j) % 40] = baseroll[j+1]
# jail for rolling doubles
for i in range(40):
    transition[i][10] += baseroll[0]
# G2J gets sent to jail
for i in range(40):
    transition[i][10] += transition[i][30]
    transition[i][30] = 0

# community chest
for cc in [2, 17, 33]:
    for i in range(40):
        a = transition[i][cc]
        transition[i][cc] = 14/16*a
        transition[i][0] += a/16
        transition[i][10] += a/16

# chances
R = {7: 15, 22: 25, 36: 5}
U = {7: 12, 22: 28, 36: 12}
for ch in [7, 22, 36]:
    for i in range(40):
        a = transition[i][ch]
        transition[i][ch] = a*6/16
        transition[i][0] += a/16
        transition[i][10] += a/16
        transition[i][11] += a/16
        transition[i][24] += a/16
        transition[i][39] += a/16
        transition[i][5] += a/16
        transition[i][R[ch]] += a/8
        transition[i][U[ch]] += a/16
        transition[i][(i-3) % 40] += a/16

print(sum(transition[1]), transition[1])
assert all(sum(transition[i]) - 1 < 0.00000000001 for i in range(40))
transition_matrix = np.array(transition)
transition_matrix = linalg.matrix_power(transition_matrix, 5000)
print(sum(transition_matrix[1]), sum(transition_matrix[2]))
t = [(transition_matrix[0][i], i) for i in range(40)]
list.sort(t)
print(t)
print(list(t[::-1][i][1] for i in range(3)))
