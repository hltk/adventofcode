from aocd import lines
from string import ascii_lowercase, ascii_uppercase
from itertools import starmap

def parts(l):
    return l[:len(l) // 2], l[len(l) // 2:]

def common(*x):
    return next(iter(set.intersection(*map(set, x))))

def f(x):
    return ("$" + ascii_lowercase + ascii_uppercase).index(x)

groups = list(zip(lines, lines[1:], lines[2:]))[::3]

print(sum(map(f, starmap(common, map(parts, lines)))))
print(sum(map(f, starmap(common, groups))))
