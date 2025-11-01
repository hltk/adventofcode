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
z[0] = 2
comp = IntCode(z)
u = comp.run([])
def db(x):
	print("".join(chr(y) for y in x))
M = [65,44,65,44,66,44,67,44,66,44,67,44,66,44,67,44,66,44,65,10]
u = comp.run(M)
A = [76,44,49,48,44,76,44,56,44,82,44,56,44,76,44,56,44,82,44,54,10]
u = comp.run(A)
B = [82,44,54,44,82,44,56,44,82,44,56,10]
u = comp.run(B)
C = [82,44,54,44,82,44,54,44,76,44,56,44,76,44,49,48,10]
u = comp.run(C)
db(M)
db(A)
db(B)
db(C)
print("".join(chr(x) for x in u))
u = comp.run([ord("y"),ord("\n")])
print(u[-1])
u = u[: -1]
print("".join(chr(x) for x in u))
