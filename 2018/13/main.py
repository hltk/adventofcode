# math.gcd
import sys,typing,re,random,math
from copy import deepcopy
from collections import defaultdict
sys.setrecursionlimit(100000)
def lmap(func, *iterables): return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]: return lmap(int, re.findall(r"-?\d+", s))
L=[]
for line in open(input()).readlines():
	line = line.strip('\n')
	L.append(list(line))
# Jokaiselle autolle suunta, sijainti, seuraava käännös
autot=[]
for i, line in enumerate(L):
	for j, ch in enumerate(line):
		A = "^v<>"
		if ch in A:
			dir = None
			if ch == "^": dir = 0
			if ch == "v": dir = 1
			if ch == "<": dir = 2
			if ch == ">": dir = 3
			autot.append([dir, [i, j], 0])
for i in range(len(L)):
	for j in range(len(L[i])):
		if (L[i][j] == "<") or (L[i][j] == ">"):
			L[i][j] = "-"
		if (L[i][j] == "^") or (L[i][j] == "v"):
			L[i][j] = "|"
def crash(z):
	u = set()
	for a, b, c in z:
		u.add((b[0],b[1]))
	return len(u) != len(z)
while not crash(autot):
	u = set()
	for a, b, c in autot: u.add((b[0],b[1]))
	pts = list(sorted([x[1], i] for i, x in enumerate(autot)))
	rem = set()
	for i in range(len(pts)):
		rem.add(i)
	for _, car_id in pts:
		if not car_id in rem: continue
		dir = autot[car_id][0]
		pos = autot[car_id][1]
		u.remove((pos[0],pos[1]))
		if dir == 0:
			autot[car_id][1][0] -= 1
		elif dir == 1:
			autot[car_id][1][0] += 1
		elif dir == 2:
			autot[car_id][1][1] -= 1
		elif dir == 3:
			autot[car_id][1][1] += 1
		pos = autot[car_id][1]
		A = L[pos[0]][pos[1]]
		if A == "/":
			if dir == 0: dir = 3
			elif dir == 1: dir = 2
			elif dir == 2: dir = 1
			elif dir == 3: dir = 0
			else:assert False
		if A == "\\":
			if dir == 0: dir = 2
			elif dir == 1: dir = 3
			elif dir == 2: dir = 0
			elif dir == 3: dir = 1
			else:assert False
		md = autot[car_id][2]
		if A == "+":
			if md == 0:
				if dir == 0: dir = 2
				elif dir == 1: dir = 3
				elif dir == 2: dir = 1
				elif dir == 3: dir = 0
				else:assert False
			if md == 2:
				if dir == 0: dir = 3
				elif dir == 1: dir = 2
				elif dir == 2: dir = 0
				elif dir == 3: dir = 1
				else:assert False
			autot[car_id][2] += 1
			autot[car_id][2] %= 3
		autot[car_id][0] = dir
		if (pos[0],pos[1]) in u:
			ax=bx=0
			for i in rem:
				if i == car_id:continue
				x = autot[i]
				if x[1] == pos:
					ax=i
					bx=car_id
					break
			rem.remove(ax)
			rem.remove(bx)
			u.remove((pos[0],pos[1]))
		else:
			u.add((pos[0],pos[1]))
	autot2 = []
	for u in rem:
		autot2.append(autot[u])
	autot = deepcopy(autot2)
	# print("tick", len(autot))
	if len(autot) == 1: break
  

	"""
	# debug print
	U = deepcopy(L)
	for a, b, c in autot:
		U[b[0]][b[1]] = "^v<>"[a]
	print("\n".join(["".join(x) for x in U]))
	"""

print(autot[0][1][1],autot[0][1][0])	
"""
u = set()
for a, b, c in autot:
	if (b[0],b[1]) in u:
		print(b[1],b[0])
	u.add((b[0],b[1]))
"""
