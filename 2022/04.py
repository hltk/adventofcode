from itertools import starmap
import re

from aocd import lines
from more_itertools import chunked


def f(a, b):
    return set(range(a, b + 1))


def ints(line):
    return tuple(map(int, re.findall(r"\d+", line)))


def contained(r1, r2):
    return (f(*r1) & f(*r2)) in [f(*r1), f(*r2)]


def overlaps(r1, r2):
    return len(f(*r1) & f(*r2)) > 0


ranges = list(map(lambda x: list(chunked(ints(x), 2)), lines))

print(sum(starmap(contained, ranges)))
print(sum(starmap(overlaps, ranges)))
