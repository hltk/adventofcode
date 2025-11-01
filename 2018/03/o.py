import re
import typing
def lmap(func, *iterables):
	return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]:
	return lmap(int, re.findall(r"-?\d+", s))
M = 5000
N = 1295
grid = [[0 for x in range(M)] for x in range(M)]
L = []
for x in range(N):
	u = input()
	u = ints(u)
	L.append([u[0], u[1 : 3], u[3 : ]])
	u = u[1 : ]
	a = u[0 : 2]
	b = u[2 : ]
	
	for i in range(a[0], a[0] + b[0]):
		for j in range(a[1], a[1] + b[1]):
			grid[i][j] += 1
	
for id, a, b in L:
	ok = 1
	for i in range(a[0], a[0] + b[0]):
		for j in range(a[1], a[1] + b[1]):
			if grid[i][j] > 1:
				ok = 0
	if ok:
		print(id)
