from aocd import lines
from more_itertools import split_at


def compare(a, b):
    match a, b:
        case int(), int():
            return a < b
        case int(), list():
            return compare([a], b)
        case list(), int():
            return compare(a, [b])
        case [x, *xs], [y, *ys]:
            if x != y:
                return compare(x, y)
            else:
                return compare(xs, ys)
        case _:
            return a == [] and b > []


items = [eval(line) if line else None for line in lines]
pairs = split_at(items, lambda x: x == None)
print(sum(i for i, p in enumerate(pairs, start=1) if compare(*p)))

packets = [[[2]], [[6]]]
ind = lambda v: sum(p != None and compare(p, v) for p in items) + 1
i0, i1 = map(ind, packets)
print(i0 * (i1 + 1))
