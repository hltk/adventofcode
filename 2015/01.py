from aocd import data

print(sum(1 if c == '(' else -1 for c in data))

from itertools import accumulate

print(next(i + 1 for i, x in enumerate(accumulate(1 if c == '(' else -1 for c in data)) if x < 0))
