from copy import deepcopy
grid = [[]for x in range(5)]
for i, line in enumerate(open("input").readlines()):
    for c in line.strip():
        grid[i].append(int(c == '#'))
def hash(grid):
    su = 0
    for x in range(25):
        i, j = x // 5, x % 5
        if grid[i][j]:
            su += 2 ** x
    return su
def simulate(grid):
    ret = deepcopy(grid)
    def get(y, x):
        if not 0 <= y < 5 or not 0 <= x < 5:
            return 0
        return grid[y][x]
    for i in range(5):
        for j in range(5):
            amt = get(i - 1, j) + get(i + 1, j) + get(i, j - 1) + get(i, j + 1)
            if grid[i][j] and amt != 1:
                ret[i][j] = 0
            elif not grid[i][j] and 1 <= amt <= 2:
                ret[i][j] = 1
    return ret
vis = set()
while True:
    if hash(grid) in vis:
        print(hash(grid))
        exit()
    vis.add(hash(grid))
    grid = simulate(grid)
