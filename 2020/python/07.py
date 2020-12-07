import operator
import re
from collections import defaultdict
from functools import reduce

from aocd import data

rg = defaultdict(list)
g = defaultdict(list)

for line in data.split("\n"):
    a = re.match(r"^(.*) bags contain", line)[1]
    for cnt, b in re.findall(r"(\d+) ([a-z ]+) bags?", line):
        rg[b].append(a)
        g[a].append((b, int(cnt)))

p1 = lambda node: reduce(operator.or_, map(p1, rg[node]), {node})
print(len(p1('shiny gold')) - 1)

p2 = lambda node: 1 + sum(p2(u) * cnt for u, cnt in g[node])
print(p2('shiny gold') - 1)
