from aocd import data

lines = data.split("\n")

n = len(lines[0])

occ = [0 for _ in range(n)]

from copy import deepcopy

oxy = deepcopy(lines)

for i in range(n):
    occ = 0
    for u in oxy:
        occ += u[i] == "1"
    bit = int(occ * 2 >= len(oxy))
    noxy = []
    for u in oxy:
        if int(u[i]) == bit:
            noxy.append(deepcopy(u))
    oxy = noxy

X = oxy[0]
oxy = deepcopy(lines)

for i in range(n):
    if len(oxy) == 1: break
    occ = 0
    for u in oxy:
        occ += u[i] == "1"
    bit = int(not (occ * 2 >= len(oxy)))
    noxy = []
    for u in oxy:
        if int(u[i]) == bit:
            noxy.append(deepcopy(u))
    oxy = noxy

print(int(X, 2) * int(oxy[0], 2))
