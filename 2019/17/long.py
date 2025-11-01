from collections import defaultdict
import sys,typing,re,random,math,functools,itertools
from copy import deepcopy
sys.setrecursionlimit(100000)
def lmap(func, *iterables): return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]: return lmap(int, re.findall(r"-?\d+", s))
def get_bounds(z):
	min_x = min(a[0] for a in z)
	max_x = max(a[0] for a in z)
	min_y = min(a[1] for a in z)
	max_y = max(a[1] for a in z)
	return min_x, max_x, min_y, max_y
def print_grid(z):
	min_x, max_x, min_y, max_y = get_bounds(z)
	s = ""
	for j in range(min_y, max_y+1):
		for i in range(min_x, max_x+1):
			s += " #23"[z[(i,j)]]
	s += "\n"
	print(s)
class IntCode:
	def __init__(self, prog):
		self.mem= defaultdict(int, enumerate(prog))
		self.numpars = {99: 0, 1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1}
		self.pc = 0
		self.off = 0
		self.halted = False
		self.inp = []
	def run(self, addinp):
		self.inp.extend(addinp)
		self.out = []
		#  break when there's no input
		while self.mem[self.pc] != 99 and (len(self.inp) or self.mem[self.pc] % 100 != 3):
			self.vals, self.locs = [], []
			self.op = self.mem[self.pc]
			self.pc += 1
			self.md = self.op // 100
			for i in range(self.numpars[self.op % 100]):
				self.mode = self.md % 10
				self.md //= 10
				if self.mode == 0:
					self.vals += [self.mem[self.mem[self.pc]]]
					self.locs += [self.mem[self.pc]]
				elif self.mode == 1:
					self.vals += [self.mem[self.pc]]
					self.locs += [None]
				elif self.mode == 2:
					self.vals += [self.mem[self.mem[self.pc] + self.off]]
					self.locs += [self.mem[self.pc] + self.off]
				else: assert False
				self.pc += 1
			self.op %= 100
			if self.op == 1:
				self.mem[self.locs[2]] = self.vals[0] + self.vals[1]
			elif self.op == 2:
				self.mem[self.locs[2]] = self.vals[0] * self.vals[1]
			elif self.op == 3:
				self.mem[self.locs[0]] = self.inp.pop(0)
			elif self.op == 4:
				self.out.append(self.vals[0])
			elif self.op == 5:
				if self.vals[0]: self.pc = self.vals[1]
			elif self.op == 6:
				if not self.vals[0]: self.pc = self.vals[1]
			elif self.op == 7:
				self.mem[self.locs[2]] = int(self.vals[0] < self.vals[1])
			elif self.op == 8:
				self.mem[self.locs[2]] = int(self.vals[0] == self.vals[1])
			elif self.op == 9:
				self.off += self.vals[0]
			else: assert False
		if self.mem[self.pc] == 99:
			self.halted = True
		return self.out
z = ints(open('input').readlines()[0])
# z[0] = 2
comp = IntCode(z)
u = "".join(chr(x) for x in comp.run([]))
u = u.split('\n')
u = [x for x in u if x]
u = [list(x) for x in u]
pos = None
lol = set()
for i in range(len(u)):
	for j in range(len(u[i])):
		if u[i][j] == '^':
			pos = (i, j)
		if u[i][j] == '#' or u[i][j] == '^':
			lol.add((i, j))
assert pos != None
vis = set()
cur = []
# left, up, right, down
dir = 1
dir_add = [(0, -1), (-1, 0), (0, 1), (1, 0)]
def add_pos(x, y):
	return (x[0] + y[0], x[1] + y[1])
while vis != lol:
	#print(pos)
	u[pos[0]][pos[1]] = "O"
	#print("\n".join("".join(x) for x in u))
	vis.add(pos)
	if vis == lol:break
	k = add_pos(dir_add[dir], pos)
	if k in lol:
		pos = k
		cur[-1] = (cur[-1][0], cur[-1][1] + 1)
	else:
		for j in range(4):
			if (j + 2) % 4 == dir: continue
			k = add_pos(dir_add[j], pos)
			if k in lol:
				if (dir + 1) % 4 == j:
					cur += [("R", 1)]
					pos = k
					dir = j
				elif (dir - 1 + 4) % 4 == j:
					cur += [("L", 1)]
					pos = k
					dir = j
				else: assert False
				break
	# print()
	# print(cur)
print(cur)
exit()
occ = defaultdict(int)
for i in range(len(cur)):
	for j in range(i, len(cur)):
		occ[repr(cur[i : j + 1])] += 1
# print(occ)
for k, v in sorted(occ.items(), key=lambda item: item[1], reverse=True):
	print(v, k)
def split(cur, k, rep):
	K = []
	A = []
	i = 0
	while i < len(cur):
		if len(cur) - i >= len(k) and cur[i:i+len(k)] == k:
			if A:K.append(A)
			A = []
			K.append(rep)
			i += len(k)
		else:
			A.append(cur[i])
			i += 1
	if A: K.append(A)
	return K
reps = [None] * 3
k = cur[: 5]
reps[0] = k
cur = split(cur, k, ord("A"))
ma = []
for i in range(len(cur)):
	if cur[i] != ord( "A"):
		assert reps[1] == None or reps[1] == cur[i][:3]
		reps[1] = cur[i][:3]
		ma.extend(split(cur[i], cur[i][:3], ord("B")))
	else: ma.append(cur[i])
ka = []
for i in range(len(ma)):
	if ma[i] != ord("A") and ma[i] != ord("B"):
		assert reps[2] == None or reps[2] == ma[i][:4]
		reps[2] = ma[i][:4]
		ka.extend(split(ma[i], ma[i][:4], ord("C")))
	else: ka.append(ma[i])
print(list(chr(x) for x in ka))
print(",".join(str(x) for x in ka) + ",10")
print()
for b in reps:
	y = []
	for a in b:
		y.append(a[0])
		y.append(a[1])
	print(y)
	x = ""
	for a in y:
		for p in str(a):
			x += p
	#print(x,len(x))
	x += "\n"
	print(",".join(str(ord(y)) for y in x))
exit()
print(cur)
print(len(cur))
P=set()
for x in cur:P.add(x)
print((P))
print(len(P))
exit()
p = defaultdict(int)
for i in range(len(cur)):
	for j in range(i, len(cur)):
		x = cur[i : j + 1]
		print(x)
		# p[] += 1
print(p)
