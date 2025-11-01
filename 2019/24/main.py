from copy import deepcopy
grid = [[[0for z in range(5)]for y in range(5)] for x in range(500)]
for i, line in enumerate(open("input").readlines()):
    for j, c in enumerate(line.strip()):
        grid[0][i][j] = int(c == '#')
ngrid = None
def simulate(lvl):
    global grid, ngrid
    def G(lvl, y, x):
        if (y, x) == (2, 2): return 0
        if not 0 <= y < 5 or not 0 <= x < 5: return 0
        return grid[lvl][y][x]
    for i in range(5):
        for j in range(5):
            if (i, j) == (2, 2): continue
            su = 0
            if (i, j) == (2, 3): su += sum(G(lvl + 1, x, 4) for x in range(5))
            if (i, j) == (2, 1): su += sum(G(lvl + 1, x, 0) for x in range(5))
            if (i, j) == (3, 2): su += sum(G(lvl + 1, 4, x) for x in range(5))
            if (i, j) == (1, 2): su += sum(G(lvl + 1, 0, x) for x in range(5))
            if i == 4: su += grid[lvl - 1][3][2]
            if i == 0: su += grid[lvl - 1][1][2]
            if j == 4: su += grid[lvl - 1][2][3]
            if j == 0: su += grid[lvl - 1][2][1]
            U = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            su += sum(G(lvl, i + x[0], j + x[1]) for x in U)
            if grid[lvl][i][j]:
                ngrid[lvl][i][j] = int(su == 1)
            else:
                ngrid[lvl][i][j] = int(1 <= su <= 2)
for x in range(200):
    print('starting:',x)
    ngrid = deepcopy(grid)
    for y in range(-200, 200 + 1):
        simulate(y)
    grid = ngrid
su = 0
for x in grid:
    for u in x:
        su += u.count(1)
print(su)
