from itertools import count
from aocd import data
mod = 20201227
a, b = map(int, data.split('\n'))
r = next(x for x in count(0) if pow(7, x, mod) == a)
print(pow(b, r, mod))
