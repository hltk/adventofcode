# math.gcd
# grid=defaultdict(lambda : defaultdict(int))
# @functools.lru_cache(maxsize=None)
import sys,typing,re,random,math,functools
from collections import defaultdict
from queue import*
grid = [list(line.strip()) for line in open("o").readlines()]
pos = {}
for i in range(len(grid)):
	for j in range(len(grid[i])):
		pos[grid[i][j]] = (i, j)
u = set(pos.keys()) ^ {".", "#"}
adj = defaultdict(list)
for x in u:
	vis = set()
	q = Queue()
	q.put([pos[x], set(), 0])
	while not q.empty():
		a = q.get()
		if a[0] in vis: continue
		if a[0] != pos[x] and not grid[a[0][0]][a[0][1]].isupper() and grid[a[0][0]][a[0][1]] not in "@.":
			d = 0
			for p in a[1]:
				d |= 2 ** (ord(p) - ord('a'))
			Q = grid[a[0][0]][a[0][1]]
			if not (ord('1') <= ord(Q) <= ord('4')):
				adj[x].append([grid[a[0][0]][a[0][1]], a[2], d])
		vis.add(a[0])
		for i in range(-1, 2):
			for j in range(-1, 2):
				if int(i != 0) + int(j != 0) != 1: continue
				u = (a[0][0] + i, a[0][1] + j)
				z = grid[u[0]][u[1]]
				if z == '#': continue
				if u in vis: continue
				if z.isupper() and z != '.':
					q.put([u, a[1] | set([z.lower()]), a[2] + 1])
				else: 
					q.put([u, a[1], a[2] + 1])
dist = {}
vis = set()
q = PriorityQueue()
q.put([0, 0, ('1', '2', '3', '4')])
ma = 0
vis.add((0, ('1','2','3','4')))
while not q.empty():
	a = q.get()
	cnt = 0
	for j in range(26):
		cnt += int(bool((2 ** j) & a[1]))
	if cnt == 26:
		print(a[0])
		exit()
	ma = max(ma, cnt)
	print(ma)
	for j in range(4):
		k = a[2][j]
		for x, y, z in adj[k]:
			ok = 1
			for J in range(26):
				if z & (2 ** J) > a[1] & (2 ** J):
					ok = 0
			if not ok: continue
			w = list(u for u in a[2])
			w[j] = x
			w = tuple(w)
			if (a[1] | (2 ** (ord(x) - ord('a'))), w) in vis:
				continue
			vis.add((a[1] | (2 ** (ord(x) - ord('a'))), w))
			q.put([a[0] + y, a[1] | (2 ** (ord(x) - ord('a'))) , w])
