import re
import operator
from itertools import combinations, starmap
from functools import reduce

from aocd import data

def area(line):
    ints = list(map(int, re.findall(r'-?\d+', line)))
    sides = list(starmap(operator.mul, combinations(ints, 2)))
    return min(sides) + 2 * sum(sides)

print(sum(area(line) for line in data.split("\n")))

def sperimeter(line):
    ints = list(map(int, re.findall(r'-?\d+', line)))
    a, b, _ = sorted(ints)
    return a * 2 + b * 2 + reduce(operator.mul, ints)

print(sum(sperimeter(line) for line in data.split("\n")))
