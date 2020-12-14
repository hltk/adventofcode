from utils import *

def tr(s, a, b):
    return s.translate(str.maketrans(a, b))

def main(inp):
    inp = inp.strip()
    inp = inp.split("\n")
    mem = {}
    for l in inp:
        l = tr(l, "[=]", "   ")
        tokens = l.split()
        if len(tokens) == 2:
            mask = tokens[-1]
        else:
            value = int(tokens[-1])
            add = int(tokens[1])
            add |= int(tr(mask, "X", "0"), 2)
            add &= ~int(tr(mask, "1X", "01"), 2)
            xs = [35 - i for i, x in enumerate(mask) if x == "X"]
            for subset in powerset(xs):
                val = add + sum(map(pow, repeat(2), subset))
                mem[val] = value

    print(sum(mem.values()))

from aocd import data
main(data)
