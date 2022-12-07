from aocd import lines
from collections import defaultdict

commands = "\n".join(lines).split("$ ")[1:]
path = []
sizes = defaultdict(int)

for c in commands:
    cmd, *args = c.split()
    if cmd == "ls":
        for sz in filter(lambda x: x.isnumeric(), args[::2]):
            sizes["/".join(path)] += int(sz)
    else:
        if ".." in args:
            x = path.pop()
            sizes["/".join(path)] += sizes["/".join(path + [x])]
        else:
            path += args

print(sum(filter(lambda x: x <= 100000, sizes.values())))
print(min(filter(lambda x: x >= sizes["/"] - 40000000, sizes.values())))
