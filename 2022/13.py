from aocd import lines
from more_itertools import split_at


def compare(a, b):
    match (a, b):
        case int(x), int(y):
            return x < y
        case [], []:
            return False
        case [], list(y):
            return True
        case list(x), []:
            return False
        case int(x), list(y):
            return compare([x], y)
        case list(x), int(y):
            return compare(x, [y])
        case [x, *xs], [y, *ys]:
            if x != y:
                return compare(x, y)
            else:
                return compare(xs, ys)


items = [eval(line) if line else None for line in lines]
pairs = split_at(items, lambda x: x == None)
print(sum(i for i, p in enumerate(pairs, start=1) if compare(*p)))

packets = [[[2]], [[6]]]
ind = lambda v: sum(p != None and compare(p, v) for p in items) + 1
i0, i1 = map(ind, packets)
print(i0 * (i1 + 1))
