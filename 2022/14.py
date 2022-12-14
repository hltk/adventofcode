from aocd import lines
from itertools import starmap, dropwhile, count
from more_itertools import flatten
import re
from utils import *

def points_from_line(line):
    ints = list(map(int, re.findall("\d+", line)))
    points = list(starmap(V, zip(ints[::2], ints[1::2])))
    return set(flatten(starmap(V.interpolate, zip(points, points[1:]))))

all_points = set.union(*map(points_from_line, lines))
orig_points = {*all_points}

moves = [(0, 1), (-1, 1), (1, 1)]
start = V(500, 0)
inf = 1000

while max(v.y for v in all_points) < inf:
    sand = start
    while sand.y < inf and (move := next(dropwhile(lambda x: (sand + x) in all_points, moves), None)):
        sand += move
    all_points.add(sand)

print(len(all_points - orig_points) - 1)

all_points = {*orig_points}
floor = max(v.y for v in all_points) + 2

while start not in all_points:
    sand = start
    while sand.y + 1 < floor and (move := next(dropwhile(lambda x: (sand + x) in all_points, moves), None)):
        sand += move
    all_points.add(sand)

print(len(all_points - orig_points))
