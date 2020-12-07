import re
from aocd import data
from collections import defaultdict

rg = defaultdict(list)
g = defaultdict(list)

for line in data.split("\n"):
    a = re.match(r"^(.*) bags contain", line)[1]
    for cnt, b in re.findall(r"(\d+) ([a-z ]+) bags?", line):
        rg[b].append(a)
        g[a].append((b, int(cnt)))

def p1():
    def dfs(node):
        seen = {node}
        for u in rg[node]:
            seen |= dfs(u)
        return seen

    return len(dfs('shiny gold')) - 1

print(p1())

def p2():
    def dfs(node):
        tot = 1
        for u, cnt in g[node]:
            tot += dfs(u) * cnt
        return tot

    return dfs('shiny gold') - 1

print(p2())
