import re
from collections import Counter

def main():
    from aocd import data

    lines = data.split("\n")

    nodes = set()
    parent = {}
    children = {}
    weight = {}

    for line in lines:
        line = re.sub('[->(),]', '', line)
        tokens = line.split()
        n = tokens[0]
        weight[n] = int(tokens[1])
        children[n] = tokens[2:]
        for u in children[n]:
            parent[u] = n
        nodes.add(n)

    root = list(nodes - set(parent.keys()))[0]

    # part 1
    print(root)

    # part 2
    def dfs(node):
        vals = [dfs(c) for c in children[node]]
        if vals and len(set(vals)) != 1:
            com, oth = [k for k,_ in Counter(vals).most_common(2)]
            x = [u for v, u in zip(vals, children[node]) if v == oth][0]
            weight[x] += com - oth
            print(weight[x])
            return weight[node] + com * len(children[node])
        return weight[node] + sum(vals)

    dfs(root)

main()
