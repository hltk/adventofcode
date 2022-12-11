from aocd import data
from aocd import lines
from operator import add, sub, methodcaller
from more_itertools import flatten


def norm(x):
    return x // abs(x) if x else 0


def add_vec(a, b):
    return tuple(map(add, a, b))


def sub_vec(a, b):
    return tuple(map(sub, a, b))


mov = dict(zip("UDLR", [(1, 0), (-1, 0), (0, -1), (0, 1)]))

make_moves = lambda line: [line.split()[0]] * int(line.split()[1])
moves = list(flatten(map(make_moves, lines)))


def simulate(*tails):
    nodes = [[(0, 0) for _ in range(max(tails))]]

    for d in moves:
        row = nodes[-1][:]
        row[0] = add_vec(row[0], mov[d])
        for i in range(1, len(row)):
            diff = sub_vec(row[i - 1], row[i])
            norm_diff = tuple(map(norm, diff))
            row[i] = add_vec(row[i], norm_diff if max(map(abs, diff)) > 1 else (0, 0))
        nodes.append(row)

    return [*map(lambda i: len({*[*zip(*nodes)][i - 1]}), tails)]


print(*simulate(2, 10))
