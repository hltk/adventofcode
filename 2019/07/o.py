class IntCode():
	def __init__(self):
		self.a=[3,8,1001,8,10,8,105,1,0,0,21,34,47,72,81,94,175,256,337,418,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,2,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99]
		#self.a=[3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
		#self.a=[3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
		self.x=0
		self.done = False
		self.input=[]
		self.output=[]
		self.waiting=False
	def isdone(self): return self.x >= len(self.a) or self.done
	def isoutput(self): return len(self.output)
	def getoutput(self):
		a = [x for x in self.output]
		self.output = []
		return a
	def addinput(self, y):
		self.waiting=False
		self.input.append(y)
	def step(self):
		if self.isdone(): return -1
		while self.x < len(self.a):
			u = str(self.a[self.x])
			if len(u) < 5: u = "0" * (5 - len(u)) + u
			op = int(u[-2 : ])
			if op == 1:
				if u[2] == "0": param1 = self.a[self.a[self.x + 1]]
				else: param1 = self.a[self.x + 1]
				if u[1] == "0": param2 = self.a[self.a[self.x + 2]]
				else: param2 = self.a[self.x + 2]
				self.a[self.a[self.x + 3]] = param1 + param2
				self.x += 4
			elif op == 2:
				if u[2] == "0": param1 = self.a[self.a[self.x + 1]]
				else: param1 = self.a[self.x + 1]
				if u[1] == "0": param2 = self.a[self.a[self.x + 2]]
				else: param2 = self.a[self.x + 2]
				self.a[self.a[self.x + 3]] = param1 * param2
				self.x += 4
			elif op == 3:
				assert not self.waiting
				if len(self.input) == 0:
					self.waiting=True
					return 0
				self.a[self.a[self.x + 1]] = self.input[0]
				self.input = self.input[1:]
				self.x += 2
			elif op == 4:
				if u[2] == "0": self.output.append(self.a[self.a[self.x + 1]])
				else: self.output.append(self.a[self.x + 1])
				self.x += 2
				return 0
			elif op == 5:
				if u[2] == "0": param1 = self.a[self.a[self.x + 1]]
				else: param1 = self.a[self.x + 1]
				if u[1] == "0": param2 = self.a[self.a[self.x + 2]]
				else: param2 = self.a[self.x + 2]
				if param1 != 0: self.x = param2
				else: self.x += 3
			elif op == 6:
				if u[2] == "0": param1 = self.a[self.a[self.x + 1]]
				else: param1 = self.a[self.x + 1]
				if u[1] == "0": param2 = self.a[self.a[self.x + 2]]
				else: param2 = self.a[self.x + 2]
				if param1 == 0: self.x = param2
				else: self.x += 3
			elif op == 7:
				if u[2] == "0": param1 = self.a[self.a[self.x + 1]]
				else: param1 = self.a[self.x + 1]
				if u[1] == "0": param2 = self.a[self.a[self.x + 2]]
				else: param2 = self.a[self.x + 2]
			elif op == 8:
				if u[2] == "0": param1 = self.a[self.a[self.x + 1]]
				else: param1 = self.a[self.x + 1]
				if u[1] == "0": param2 = self.a[self.a[self.x + 2]]
				else: param2 = self.a[self.x + 2]
				if u[0] == "0": param3 = self.a[self.x + 3]
				else: param3 = self.x + 3
				if param1 == param2: self.a[param3] = 1
				else: self.a[param3] = 0
				self.x += 4
			elif op == 99:
				self.done = 1
				return -1
			else:
				assert False
		print("RESTART REQUIRED (shouldn't happen)")
		return -1

import itertools
perm = list(itertools.permutations(range(5)))
u=0
for a in perm:
	amps = []
	for x in range(5):
		amps.append(IntCode())
	for x in range(5):
		amps[x].addinput(a[x] + 5)
	amps[0].addinput(0)
	it = 0
	lst=0
	while 1:
		#print("running",it)
		ret = amps[it].step()
		a = amps[it].getoutput()
		if it == 4: lst=a[0]
		if not a:break
		assert len(a) == 1
		amps[(it + 1) % 5].addinput(a[0])
		it = (it + 1) % 5
	u=max(u,lst)
	print(lst)
print()
print(u)
