from utils import *
from aocd import data, submit

p1 = 0
p2 = 0

for line in data.split("\n"):
    match = re.fullmatch(r'(\d+)-(\d+) (.): (.+)', line)
    a, b, c, s = match.groups()
    a, b = map(int, (a, b))
    p1 += a <= s.count(c) <= b
    p2 += (s[a - 1] + s[b - 1]).count(c) == 1

print(p1)

print(p2)
