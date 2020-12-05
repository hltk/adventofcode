import re
from collections import defaultdict

def main():
    from aocd import data

    lines = data.split("\n")

    regs = defaultdict(int)

    maxs = [0]

    for line in lines:
        R = r'(\w+) (inc|dec) (-?\d+) if (\w+) ((>=|<=|!=|==|<|>) (-?\d+))'
        g = re.match(R, line).groups()
        if eval(f"{regs[g[3]]} {g[4]}"):
            regs[g[0]] += int(g[2]) * (1 if g[1] == "inc" else -1)
        maxs.append(max(regs.values()))

    # part 1
    print(maxs[-1])

    # part 2
    print(max(maxs))

main()
