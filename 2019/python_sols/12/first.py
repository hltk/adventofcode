import typing,re
def lmap(func, *iterables): return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]: return lmap(int, re.findall(r"-?\d+", s))
L = []
for line in open("input").readlines():
	u = ints(line)
	u += [0] * 3
	L.append(u + [0] * 3)
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
for x in range(1000): L = step(L)
res = sum(sum(map(abs, a[:3]))*sum(map(abs, a[3:])) for a in L)
print(res)
