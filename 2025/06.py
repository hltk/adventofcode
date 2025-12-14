from aocd import data
from math import prod
from functools import reduce

data = data.splitlines()
*eq, op = [l.split() for l in data]

print(sum((prod if o < "+" else sum)(map(int, c)) for c, o in zip(zip(*eq), op)))

f = lambda x, l: x + [[]] if set(l) == {" "} else x[:-1] + [x[-1] + [l]]
blk = reduce(f, zip(*data), [[]])

print(sum((sum if "+" in b[0] else prod)(int(''.join(c for c in r if c > "+")) for r in b) for b in blk))
