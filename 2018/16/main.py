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
def addr(mem, A, B, C):
	mem[C] = mem[A] + mem[B]
def addi(mem, A, B, C):
	mem[C] = mem[A] + B
def mulr(mem, A, B, C):
	mem[C] = mem[A] * mem[B]
def muli(mem, A, B, C):
	mem[C] = mem[A] * B
def banr(mem, A, B, C):
	mem[C] = mem[A] & mem[B]
def bani(mem, A, B, C):
	mem[C] = mem[A] & B
def borr(mem, A, B, C):
	mem[C] = mem[A] | mem[B]
def bori(mem, A, B, C):
	mem[C] = mem[A] | B
def setr(mem, A, B, C):
	mem[C] = mem[A]
def seti(mem, A, B, C):
	mem[C] = A
def gtir(mem, A, B, C):
	mem[C] = int(A > mem[B])
def gtri(mem, A, B, C):
	mem[C] = int(mem[A] > B)
def gtrr(mem, A, B, C):
	mem[C] = int(mem[A] > mem[B])
def eqir(mem, A, B, C):
	mem[C] = int(A == mem[B])
def eqri(mem, A, B, C):
	mem[C] = int(mem[A] == B)
def eqrr(mem, A, B, C):
	mem[C] = int(mem[A] == mem[B])
ins = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
k = open("input").readlines()
u = k[: 2340]
O = k[2340 : ]
res = 0
nums = {}
for i in range(0, len(u), 3):
	A = ints(u[i])
	B = ints(u[i + 1])
	C = ints(u[i + 2])
	cnt = 0
	P = set()
	for i, f in enumerate(ins):
		D = deepcopy(A)
		f(D, B[1], B[2], B[3])
		if D == C: P.add(i)
	if B[0] not in nums:
		nums[B[0]] = P
	else: nums[B[0]] = nums[B[0]] & P
while True:
	ok = 1
	for v in nums.values():
		if len(v) > 1:
			ok = 0
	if ok: break
	F = []
	for v in nums.values():
		if len(v) == 1:
			F.append(next(iter(v)))
	assert len(F) != 0
	for k in nums.keys():
		if len(nums[k]) == 1:
			continue
		for o in F:
			if o in nums[k]:
				nums[k].remove(o)
for k in nums.keys():
	nums[k] = next(iter(nums[k]))
mem = [0] * 4
for line in O:
	line = ints(line)
	ins[nums[line[0]]](mem, line[1], line[2], line[3])
print(mem[0])
