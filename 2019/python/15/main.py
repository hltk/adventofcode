from collections import defaultdict
import sys,typing,re,random,math,functools,itertools
from copy import deepcopy
sys.setrecursionlimit(100000)
def lmap(func, *iterables): return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]: return lmap(int, re.findall(r"-?\d+", s))
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
def printgridfromddict(dc):
	z = dc.keys()
	xmi = min([x[1]for x in z])
	ymi = min([x[0]for x in z])
	xma = max([x[1]for x in z])
	yma = max([x[0]for x in z])
	xsz = xma - xmi + 1
	ysz = yma - ymi + 1
	o=[[" "for x in range(xsz)] for y in range(ysz)]
	for u in z:
		o[u[0] - ymi][u[1] - xmi] = "#" if dc[(u[0],u[1])] else " "
		if dc[(u[0], u[1])] == 2:
			o[u[0] - ymi][u[1] - xmi] = "O"
		if dc[(u[0], u[1])] == 3:
			o[u[0] - ymi][u[1] - xmi] = "S"
	print("\n".join("".join(u)for u in o))
vis = set()
z = ints(open('input').readlines()[0])
comp = IntCode(z)
grid = defaultdict(int)
vis.add((0, 0))
pos = None
def haku(y, x):
	global comp
	global pos
	if (y + 1, x) not in vis:
		u = comp.run([1])
		vis.add((y + 1, x))
		if u[0] == 0:
			grid[(y + 1, x)] = 1
		else:
			if u[0] == 2:
				pos = (y + 1, x)
				grid[(y + 1, x)] = 2
			haku(y + 1, x)
			assert comp.run([2]) != 0
	if (y - 1, x) not in vis:
		u = comp.run([2])
		vis.add((y - 1, x))
		if u[0] == 0:
			grid[(y - 1, x)] = 1
		else:
			if u[0] == 2:
				pos = (y - 1, x)
				grid[(y - 1, x)] = 2
			haku(y - 1, x)
			assert comp.run([1]) != 0
	if (y, x + 1) not in vis:
		u = comp.run([4])
		vis.add((y, x + 1))
		if u[0] == 0:
			grid[(y, x + 1)] = 1
		else:
			if u[0] == 2:
				pos = (y, x + 1)
				grid[(y, x + 1)] = 2
			haku(y, x + 1)
			assert comp.run([3]) != 0
	if (y, x - 1) not in vis:
		u = comp.run([3])
		vis.add((y, x - 1))
		if u[0] == 0:
			grid[(y, x - 1)] = 1
		else:
			if u[0] == 2:
				pos = (y, x - 1)
				grid[(y, x - 1)] = 2
			haku(y, x - 1)
			assert comp.run([4]) != 0
		
haku(0, 0)
grid[(0, 0)] = 3
# printgridfromddict(grid)
import queue
q = queue.Queue()
start = pos #(0, 0)
q.put(start)
dist = defaultdict(lambda :10**10)
vis = defaultdict(int)
dist[start] = 0
vis[start] = 1
while not q.empty():
	y, x = q.get()
	if grid[(y + 1, x)] != 1:
		if not vis[(y + 1, x)]:
			dist[(y + 1, x)] = dist[(y, x)] + 1
			vis[(y + 1, x)] = 1
			q.put((y + 1, x))
	if grid[(y - 1, x)] != 1:
		if not vis[(y - 1, x)]:
			dist[(y - 1, x)] = dist[(y, x)] + 1
			vis[(y - 1, x)] = 1
			q.put((y - 1, x))
	if grid[(y, x + 1)] != 1:
		if not vis[(y, x + 1)]:
			dist[(y, x + 1)] = dist[(y, x)] + 1
			vis[(y, x + 1)] = 1
			q.put((y, x + 1))
	if grid[(y, x - 1)] != 1:
		if not vis[(y, x - 1)]:
			dist[(y, x - 1)] = dist[(y, x)] + 1
			vis[(y, x - 1)] = 1
			q.put((y, x - 1))
print(max(dist.values()))
#  print(dist[pos])
