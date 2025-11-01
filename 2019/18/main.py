# math.gcd
# grid=defaultdict(lambda : defaultdict(int))
# @functools.lru_cache(maxsize=None)
import sys,typing,re,random,math,functools
from collections import defaultdict
from copy import deepcopy
sys.setrecursionlimit(100000)
def lmap(func, *iterables): return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]: return lmap(int, re.findall(r"-?\d+", s))
def print_grid(z):
	min_x = min(a[1] for a in z)
	max_x = max(a[1] for a in z)
	min_y = min(a[0] for a in z)
	max_y = max(a[0] for a in z)
	for i in range(min_y, max_y+1):
		s = ""
		for j in range(min_x, max_x+1):
			s += " #23456789"[z[(i,j)]]
		print(s)
grid = [list(line.strip()) for line in open("lmao").readlines()]
pos = None
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == '@': pos = (i, j)
assert pos != None
vis = set()
def haku(x, prev):
	global vis
	assert x not in vis
	vis.add(x)
	fill = int(grid[x[0]][x[1]] == '.')
	for i in range(-1, 2):
		for j in range(-1, 2):
			if int(i != 0) + int(j != 0) != 1: continue
			u = (x[0] + i, x[1] + j)
			if grid[u[0]][u[1]] == '#': continue
			if u == prev: continue
			fill &= haku(u, x)
	if fill:
		grid[x[0]][x[1]] = '#'
		return 1
	return 0
haku(pos, pos)
print("\n".join("".join(x) for x in grid))
