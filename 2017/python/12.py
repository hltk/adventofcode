from collections import defaultdict

def main():
    from aocd import data
    g = defaultdict(list)

    for line in data.split("\n"):
        line = line.replace(',', '')
        node, _, *c = line.split()
        for x in c:
            g[node].append(x)
            g[x].append(node)

    vis = set()
    def dfs(s):
        if s in vis:
            return 0
        vis.add(s)
        r = 1
        for u in g[s]:
            r += dfs(u)
        return r

    groups = {}
    for s in g.keys():
        if s in vis:
            continue
        groups[s] = dfs(s)

    # part 1
    print(groups['0'])

    # part 2
    print(len(groups))

main()
