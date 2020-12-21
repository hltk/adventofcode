from collections import defaultdict
from aocd import data
from math import floor, sqrt

prog = list(map(lambda x: x.split(), data.split("\n")))
reg = {x: 0 for x in "abcdefgh"}
it = 0
mul = 0

def G(x):
    return reg[x] if x in reg else int(x)

while 0 <= it < len(prog):
    a, b, c = prog[it]
    if a == 'set': reg[b] = G(c)
    if a == 'sub': reg[b] -= G(c)
    if a == 'mul': reg[b] *= G(c); mul += 1
    if a == 'jnz': it += int(c) - 1 if G(b) != 0 else 0
    it += 1

print(mul)

reg = {x: 0 for x in reg.keys()}
it = 0
reg['a'] = 1

def prime(x):
    return x > 1 and all([x % y != 0 for y in range(2, floor(sqrt(x)) + 1)])

while 0 <= it < len(prog):
    if it == 8:
        reg['f'] = int(prime(reg['b']))
        it += 16
        continue
    a, b, c = prog[it]
    if a == 'set': reg[b] = G(c)
    if a == 'sub': reg[b] -= G(c)
    if a == 'mul': reg[b] *= G(c)
    if a == 'jnz': it += int(c) - 1 if G(b) != 0 else 0
    it += 1

print(reg['h'])
