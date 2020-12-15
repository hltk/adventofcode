from itertools import repeat
from more_itertools import powerset
from parse import parse

def tr(s, a, b):
    return s.translate(str.maketrans(a, b))

def main(inp):
    inp = inp.strip()
    mem = {}
    for l in inp.split("\n"):
        tokens = l.split()
        if p := parse("mask = {}", l):
            mask = p[0]
        else:
            add, value = parse("mem[{:d}] = {:d}", l)
            add |= int(tr(mask, "X", "0"), 2)
            add &= ~int(tr(mask, "1X", "01"), 2)
            xs = [35 - i for i, x in enumerate(mask) if x == "X"]
            for subset in powerset(xs):
                val = add + sum(map(pow, repeat(2), subset))
                mem[val] = value

    print(sum(mem.values()))

from aocd import data
main(data)
