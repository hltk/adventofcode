from aocd import data
from more_itertools import windowed

f = lambda c: next(i + c for i, w in  enumerate(windowed(data, c)) if len({*w}) == c)

print(f(4))
print(f(14))
