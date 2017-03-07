# probability of drawing blue = 1/(1+turn)
# probability of drawing red  = turn/(1+turn)
# turn = 1, 2, 3, ..., 15
# prize fund = floor(1/probability of player winning)
#
# case 1 turn
# blue, red
# 1st turn
# 1/2, 1/2
# 1 blue = 1/2
# 0 blue = 1/2
#
# case 2 turns
# 2nd turn
# 1/3, 2/3
# 2 blue = 1/2*1/3        =1/6
# 1 blue = 1/2*1/3+1/2*2/3=1/2
# 0 blue =        +1/2*2/3=1/3
#
# case 3 turns
# 3rd turn
# 1/4, 3/4
# 3 blue = 1/6*1/4        =1/24
# 2 blue = 1/2*1/4+1/6*3/4=1/4
# 1 blue = 1/3*1/4+1/2*3/4=11/24
# 0 blue =        +1/3*3/4=1/4
#
# case 4 turns
# 4th turn
# 1/5, 4/5
# 4 blue = 1/24 *1/5            =1/120
# 3 blue = 1/4  *1/5+1/24 *4/5  =1/12
# 2 blue = 11/24*1/5+1/4  *4/5  =7/24
# 1 blue = 1/4  *1/5+11/24*4/5  =5/12
# 0 blue =          +1/4  *4/5  =1/5
# b = [p(0 blue), p(1 blue), p(2 blue), ..., p(n-1 blue), p(n blue)]
t = 15
b = [1/2, 1/2]
for c in range(t-1):
    t = len(b)
    b = [b[0]*t/(1+t)] + list(b[i+1]*t/(1+t)+b[i]/(1+t) for i in range(len(b)-1)) + [b[-1]/(1+t)]
pw = sum(i for i in b[::-1][:len(b)//2])
print(int(1/pw))