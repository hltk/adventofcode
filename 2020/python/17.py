def neighbours(x, y, z, w):
    for xi in range(-1, 2):
        for yi in range(-1, 2):
            for zi in range(-1, 2):
                for wi in range(-1, 2):
                    if xi != 0 or yi != 0 or zi != 0 or wi != 0:
                        yield (x + xi, y + yi, z + zi, w + wi)

def main(inp):
    inp = inp.strip()
    inp = inp.split('\n')
    n, m = len(inp), len(inp[0])
    act = set()
    for i in range(n):
        for j in range(m):
            if inp[i][j] == '#':
                act.add((i, j, 0, 0))
    for t in range(6):
        nact = set()
        to_test = act.copy()
        for x, y, z, w in act:
            for nx, ny, nz, nw in neighbours(x, y, z, w):
                to_test.add((nx, ny, nz, nw))
        for x, y, z, w in to_test:
            cnt = sum(map(act.__contains__, neighbours(x, y, z, w)))
            if (x, y, z, w) in act and 2 <= cnt <= 3:
                nact.add((x, y, z, w))
            if (x, y, z, w) not in act and cnt == 3:
                nact.add((x, y, z, w))
        act = nact
    print(len(act))

from aocd import data
main(data)
