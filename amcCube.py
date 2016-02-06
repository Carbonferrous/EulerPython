import itertools

ident = tuple(range(8))
xrot = (1, 2, 3, 0, 5, 6, 7, 4)
yrot = (3, 2, 6, 7, 0, 1, 5, 4)
zrot = (1, 5, 6, 2, 0, 4, 7, 3)

faces = [(0, 1, 2, 3), (1, 2, 5, 6), (2, 3, 6, 7), (4, 5, 6, 7), (0, 3, 4, 7), (0, 1, 4, 5)]

def permute(l, p):
    return tuple(l[x] for x in p)

def all_equal(l):
    try:
        l = iter(l)
        n = next(l)
        return all(n == r for r in l)
    except StopIteration: return True

xrots = [ident, xrot, permute(xrot, xrot), permute(permute(xrot, xrot), xrot)]
yrots = [ident, yrot, permute(yrot, yrot), permute(permute(yrot, yrot), yrot)]
zrots = [ident, zrot, permute(zrot, zrot), permute(permute(zrot, zrot), zrot)]

vxs = set(filter(lambda vx: all_equal(sum(map(vx.__getitem__, face)) for face in faces), itertools.permutations(range(8))))
final = []
while vxs:
    vx = vxs.pop()
    final.append(vx)
    for xr in xrots:
        for yr in yrots:
            for zr in zrots:
                vxs.discard(permute(permute(permute(vx, xr), yr), zr))

print(len(final))
for vx in final:
    print(vx)
