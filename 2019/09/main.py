U = list(map(int, open('input').read().split(",")))
G = U + [0] * 100000
numpars = {99: 0, 1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1}
def run(prog):
	pc = off = 0
	while prog[pc] != 99:
		vals, locs = [], []
		op = prog[pc]
		pc += 1
		md = op // 100
		for i in range(numpars[op % 100]):
			mode = md % 10
			md //= 10
			if mode == 0:
				vals += [prog[prog[pc]]]
				locs += [prog[pc]]
			elif mode == 1:
				vals += [prog[pc]]
				locs += [None]
			elif mode == 2:
				vals += [prog[prog[pc] + off]]
				locs += [prog[pc] + off]
			else: assert False
			pc += 1
		op %= 100
		if op == 1:
			prog[locs[2]] = vals[0] + vals[1]
		elif op == 2:
			prog[locs[2]] = vals[0] * vals[1]
		elif op == 3:
			prog[locs[0]] = int(input("input: "))
		elif op == 4:
			print("ans:", vals[0])
		elif op == 5:
			if vals[0]: pc = vals[1]
		elif op == 6:
			if not vals[0]: pc = vals[1]
		elif op == 7:
			prog[locs[2]] = int(vals[0] < vals[1])
		elif op == 8:
			prog[locs[2]] = int(vals[0] == vals[1])
		elif op == 9:
		 	off += vals[0]
		else: assert False
	print("halted")
run(G)
