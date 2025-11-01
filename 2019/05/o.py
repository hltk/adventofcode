from collections import defaultdict
import sys,typing,re
sys.setrecursionlimit(100000)
def lmap(func, *iterables): return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]: return lmap(int, re.findall(r"-?\d+", s))
a = list(map(int, input().split()))
x = 0
while x < len(a):
	u = str(a[x])
	if len(u) < 5: u = "0" * (5 - len(u)) + u
	op = int(u[-2 : ])
	# print(x, a, u, op)
	if op == 1:
		if u[2] == "0": param1 = a[a[x + 1]]
		else: param1 = a[x + 1]
		if u[1] == "0": param2 = a[a[x + 2]]
		else: param2 = a[x + 2]
		a[a[x + 3]] = param1 + param2
		x += 4
	elif op == 2:
		if u[2] == "0": param1 = a[a[x + 1]]
		else: param1 = a[x + 1]
		if u[1] == "0": param2 = a[a[x + 2]]
		else: param2 = a[x + 2]
		a[a[x + 3]] = param1 * param2
		x += 4
	elif op == 3:
		a[a[x + 1]] = int(input())
		x += 2
	elif op == 4:
		if u[2] == "0": print(a[a[x + 1]])
		else: print(a[x + 1])
		x += 2
	elif op == 5:
		if u[2] == "0": param1 = a[a[x + 1]]
		else: param1 = a[x + 1]
		if u[1] == "0": param2 = a[a[x + 2]]
		else: param2 = a[x + 2]
		if param1 != 0: x = param2
		else: x += 3
	elif op == 6:
		if u[2] == "0": param1 = a[a[x + 1]]
		else: param1 = a[x + 1]
		if u[1] == "0": param2 = a[a[x + 2]]
		else: param2 = a[x + 2]
		if param1 == 0: x = param2
		else: x += 3
	elif op == 7:
		if u[2] == "0": param1 = a[a[x + 1]]
		else: param1 = a[x + 1]
		if u[1] == "0": param2 = a[a[x + 2]]
		else: param2 = a[x + 2]
		if u[0] == "0": param3 = a[x + 3]
		else: param3 = x + 3
		if param1 < param2: a[param3] = 1
		else: a[param3] = 0
		x += 4
	elif op == 8:
		if u[2] == "0": param1 = a[a[x + 1]]
		else: param1 = a[x + 1]
		if u[1] == "0": param2 = a[a[x + 2]]
		else: param2 = a[x + 2]
		if u[0] == "0": param3 = a[x + 3]
		else: param3 = x + 3
		if param1 == param2: a[param3] = 1
		else: a[param3] = 0
		x += 4
	elif op == 99:
	       exit(1)
	else: assert False
