import typing,re,math
from copy import deepcopy
def lmap(func, *iterables): return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]: return lmap(int, re.findall(r"-?\d+", s))
L = []
for line in open("input").readlines():
	u = ints(line)
	u += [0] * 3
	L.append(u + [0] * 3)
O = deepcopy(L)
def step(L):
	for i in range(len(L)):
		for j in range(i + 1, len(L)):
			for h in (0, 1, 2):
				if L[i][h] == L[j][h]:
					continue
				if L[i][h] < L[j][h]:
					L[i][h + 3] += 1
					L[j][h + 3] -= 1
				if L[i][h] > L[j][h]:
					L[i][h + 3] -= 1
					L[j][h + 3] += 1
	for i in range(len(L)):
		for j in (0, 1, 2):
			L[i][j] += L[i][j + 3]
	return L
cyc = [-1] * 3
for x in range(1, 1000000):
	L = step(L)
	for h in (0, 1, 2):
		if cyc[h] != -1: continue
		o1 = all(L[i][h] == O[i][h] for i in range(len(L)))
		o2 = all(L[i][h + 3] == 0 for i in range(len(L)))
		if o1 and o2:
			cyc[h] = x
lcm = lambda x, y : x // math.gcd(x, y) * y
cyc[1] = lcm(cyc[0], cyc[1])
cyc[2] = lcm(cyc[1], cyc[2])
print(cyc[2])
