from functools import partial
from itertools import product, chain
import operator

def zip_func(vec1, vec2, func):
    return tuple(func(a, b) for a, b in zip(vec1, vec2))

zip_add = partial(zip_func, func=operator.add)

def neighbours(p):
    for dp in set(product(range(-1, 2), repeat=4)) - {(0, 0, 0, 0)}:
        yield zip_add(p, dp)

def main(inp):
    inp = inp.split('\n')
    n, m = len(inp), len(inp[0])
    act = {(i, j, 0, 0) for i, j in product(range(n), range(m)) if inp[i][j] == '#'}
    for t in range(6):
        nact = set()
        to_test = set(chain.from_iterable(neighbours(p) for p in act)) | act
        for p in to_test:
            cnt = sum(map(act.__contains__, neighbours(p)))
            if cnt == 3 or (p in act and cnt == 2):
                nact.add(p)
        act = nact
    print(len(act))

from aocd import data
main(data)
