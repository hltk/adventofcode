from aocd import data
from aocd import lines
from operator import add, methodcaller
from more_itertools import flatten

def norm(x): return x // abs(x) if x else 0
def add_vec(a, b): return tuple(map(add, a, b))

mov = dict(zip("UDLR", [(1, 0), (-1, 0), (0, -1), (0, 1)]))

make_moves = lambda line: [line.split()[0]] * int(line.split()[1])
moves = list(flatten(map(make_moves, lines)))

def move_tail(head, tail):
    diff = head[0] - tail[0], head[1] - tail[1]
    norm_diff = tuple(map(norm, diff))
    if diff[1] == 0 and abs(diff[0]) > 1:
        tail = add_vec(tail, (norm_diff[0], 0))
    elif diff[0] == 0 and abs(diff[1]) > 1:
        tail = add_vec(tail, (0, norm_diff[1]))
    elif sum(map(abs, diff)) > 2:
        tail = add_vec(tail, norm_diff)
    return tail

def simulate(n):
    nodes = [(0, 0) for _ in range(n)]
    tail_pos = {nodes[-1]}

    for d in moves:
        nodes[0] = add_vec(nodes[0], mov[d])
        for i in range(1, n):
            nodes[i] = move_tail(nodes[i - 1], nodes[i])
        tail_pos.add(nodes[-1])

    return len(tail_pos)

print(simulate(2))
print(simulate(10))
