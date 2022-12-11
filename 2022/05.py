import re
from aocd import data


def ints(line):
    return tuple(map(int, re.findall(r"\d+", line)))


i, lines = data.split("\n\n")
i = [row[1::4] for row in i.split("\n") if row][:-1]
i = [*zip(*reversed(i))]
i = [list("".join(s).strip()) for s in i]

# Part 1:
# for amt, f, t in map(ints, lines.split("\n")):
#     for _ in range(amt):
#         i[t - 1].append(i[f - 1].pop())

for amt, f, t in map(ints, lines.split("\n")):
    lol = [i[f - 1].pop() for _ in range(amt)]
    for x in reversed(lol):
        i[t - 1].append(x)

print("".join(map(lambda x: x[-1], i)))
