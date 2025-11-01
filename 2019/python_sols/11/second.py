from collections import defaultdict
class IntCode:
	def __init__(self, prog):
		self.mem= defaultdict(int, enumerate(prog))
		self.numpars = {99: 0, 1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1}
		self.pc = 0
		self.off = 0
	def run(self, inp):
		self.out = []
		#  break when there's no input
		while self.mem[self.pc] != 99 and (len(inp) or self.mem[self.pc] % 100 != 3):
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
				self.mem[self.locs[0]] = inp.pop(0)
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
			return -1
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
	print("\n".join("".join(u)for u in o))

U = list(map(int, open('input').read().split(",")))
Op = IntCode(U)
grid = defaultdict(int)
grid[(0, 0)] = 1

# 0 left, 1, up, 2 right, 3 down
dir = 1
pos = (0, 0)

while 1:
	if grid[pos]: col = 1
	else: col = 0
	u = Op.run([col])
	if u == -1:
		break
	grid[pos] = u[0]
	if u[1] == 0: dir = (dir + 3) % 4
	else: dir = (dir + 1) % 4
	pos = list(pos)
	if dir == 0: pos[1] -= 1
	if dir == 1: pos[0] -= 1
	if dir == 2: pos[1] += 1
	if dir == 3: pos[0] += 1
	pos = tuple(pos)
	if u == -1:
		break

printgridfromddict(grid)
