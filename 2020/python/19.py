from collections import *
from functools import *
from parse import *

def ints(line):
    return [int(r[0]) for r in findall("{:d}", line)]

def main(inp):
    inp = inp.replace("8: 42", "8: 42 | 42 8")
    inp = inp.replace("11: 42 31", "11: 42 31 | 42 11 31")
    inp = inp.strip()
    a, b = inp.split('\n\n')
    a = a.split('\n')
    b = b.split('\n')
    edges = {}
    ans = {}
    lol = set()
    for l in a:
        i, l = l.split(": ")
        i = int(i)
        if "\"" in l:
            lol.add(i)
            ans[i] = l[1]
        else:
            edges[i] = list(map(ints, l.split(" | ")))

    @cache
    def dfs(m, s=0):
        if s in lol:
            return m == ans[s]
        for x in edges[s]:
            if len(x) == 1:
                if dfs(m, x[0]):
                    return True
            if len(x) == 2:
                for amt0 in range(1, len(m)):
                    if dfs(m[:amt0], x[0]) and dfs(m[amt0:], x[1]):
                        return True
            if len(x) == 3:
                for amt0 in range(1, len(m)):
                    for amt1 in range(amt0 + 1, len(m)):
                        if dfs(m[:amt0], x[0]) and dfs(m[amt0:amt1], x[1]) and dfs(m[amt1:], x[2]):
                            return True

        return False

    print(sum(map(dfs, b)))

from aocd import data
main(data)
