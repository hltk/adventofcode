from itertools import accumulate

from aocd import data

def mov(p, c):
    if c == '^': return (p[0] + 1, p[1])
    if c == 'v': return (p[0] - 1, p[1])
    if c == '<': return (p[0], p[1] + 1)
    if c == '>': return (p[0], p[1] - 1)

def visited(d):
    return set(accumulate(d, mov, initial=(0, 0)))

print(len(visited(data)))

print(len(visited(data[0::2]) | visited(data[1::2])))
