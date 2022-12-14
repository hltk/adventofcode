from aocd import lines
from itertools import starmap, dropwhile, count
from more_itertools import flatten
import re
from utils import *

def points_from_line(line):
    ints = list(map(int, re.findall("\d+", line)))
    points = list(starmap(V, zip(ints[::2], ints[1::2])))
    return set(flatten(starmap(V.interpolate, zip(points, points[1:]))))

moves, start = [(0, 1), (-1, 1), (1, 1)], V(500, 0)

points, placed = set.union(*map(points_from_line, lines)), set()
exists = lambda p: p in placed or p in points
floor = max(v.y for v in points) + 1

while start not in placed:
    sand = start
    while sand.y < floor and (move := next(dropwhile(lambda x: exists(sand + x), moves), None)):
        sand += move
    if sand.y == floor and max(v.y for v in placed) < floor:
        print(len(placed))
    placed.add(sand)

print(len(placed))
