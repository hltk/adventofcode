from utils import *
from aocd import data, submit

p1, p2 = 0, 0

for l in data.split("\n\n"):
    p1 += len(set(l.replace("\n", "")))

for l in data.split("\n\n"):
    p2 += len(reduce(operator.and_, map(set, l.split("\n"))))

print(p1)

print(p2)
