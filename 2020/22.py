from aocd import get_data
from itertools import count
from parse import findall
import operator


def ints(line):
    return [int(r[0]) for r in findall("{:d}", line)]


def main(inp):
    inp = inp.strip()
    a, b = inp.split('\n\n')
    a = ints(a[a.index(":"):])
    b = ints(b[b.index(":"):])

    def winner(a, b, game_id=1):
        seen = set()
        while a and b:
            state = (tuple(a), tuple(b))
            if state in seen:
                return 0, a
            seen.add(state)
            x, *a = a
            y, *b = b
            rv = 0 if x > y else 1
            if len(a) >= x and len(b) >= y:
                rv = winner(a[:x], b[:y], game_id+1)[0]
            if rv == 0:
                a = a + [x, y]
            else:
                b = b + [y, x]
        return (0, a) if a else (1, b)

    _, w = winner(a, b)
    print(sum(map(operator.mul, count(len(w), -1), w)))


main(get_data(day=22))
