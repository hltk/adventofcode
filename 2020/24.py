import itertools

movs = {
    "e":  lambda p: (p[0] + 1, p[1] - 1, p[2]),
    "w":  lambda p: (p[0] - 1, p[1] + 1, p[2]),
    "se": lambda p: (p[0], p[1] - 1, p[2] + 1),
    "sw": lambda p: (p[0] - 1, p[1], p[2] + 1),
    "nw": lambda p: (p[0], p[1] + 1, p[2] - 1),
    "ne": lambda p: (p[0] + 1, p[1], p[2] - 1),
}

def neigh(p):
    for f in movs.values():
        yield f(p)

def main(inp):
    alive = set()
    for l in inp.split('\n'):
        p = (0, 0, 0)
        i = 0
        while i < len(l):
            mov = l[i]
            i += 1
            if mov in "sn":
                mov += l[i]
                i += 1
            p = movs[mov](p)
        (alive.add if p not in alive else alive.discard)(p)
    print(len(alive))
    for t in range(100):
        def good(p):
            cnt = sum(map(alive.__contains__, neigh(p)))
            return cnt == 2 or (p in alive and cnt == 1)
        totest = itertools.chain.from_iterable(map(neigh, alive))
        alive = {p for p in totest if good(p)}
    print(len(alive))

from aocd import get_data
main(get_data(day=24))
