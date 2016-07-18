1. 20 * 30 ** (n-1) 2n-digit solutions
2. no 4n+1 solutions
3. 100*500**n 4n+3 solutions

Case 1
abcd...efgh
hgfe...dcba

a+h has no carries, one is odd, the other is even, neither are 0 - 20 possible
a h
1 2,4,6,8
2 1,3,5,7
3 2,4,6
4 1,3,5
5 2,4
6 1,3
7 2
8 1

b+g can be same as above but also 0 - 30 possible
b g
0 1,3,5,7,9
1 0,2,4,6,8
2 1,3,5,7
3 0,2,4,6
4 1,3,5
5 0,2,4
6 1,3
7 0,2
8 1
9 0

Case 3
abc...d...efg
gfe...d...cba

a+g must carry and be odd to create odd middle, one is odd, the other iss even
b+f even and carry
e+c odd and carry
d+d must not carry
