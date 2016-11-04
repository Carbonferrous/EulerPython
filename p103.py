def isspecial(A):
    return True
def nextnearopt(A):
    b = A[len(A)//2]
    A = [0] + A
    A = list(i+b for i in A)
    return A
n = 7
A = nextnearopt([11, 18, 19, 20, 22, 25])
assert len(A) == n
minsum = sum(i for i in A)
minA = A
nearbyA = [A]
for x in nearbyA:
    if sum(i for i in x) < minsum and isspecial(x):
        minsum = sum(i for i in x)
        minA = x
print(''.join(str(i) for i in minA))
