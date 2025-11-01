from math import pi, gcd, isclose
from cmath import phase
from itertools import groupby
# cmath.phase()
g = []
for line in open('input').readlines():
	line = line.strip()
	g.append(list(line))
for i, row in enumerate(g):
	for j, col in enumerate(row):
		if col != "#":
			continue
		angls = set()
		for it, rowt in enumerate(g):
			for jt, colt in enumerate(rowt):
				if it == i and jt == j:
					continue
				if colt == "#":
					ay = i - it
					ax = j - jt
					u = abs(gcd(ay, ax))
					ay //= u
					ax //= u
					angls.add((ay, ax))
		if len(angls) != 256: continue
		a = []
		for it, rowt in enumerate(g):
			for jt, colt in enumerate(rowt):
				if it == i and jt == j:
					continue
				if colt == "#":
					ay = i - it
					ax = j - jt
					a.append([complex(ay, ax), (it, jt)])
		def ang(x):
			y = phase(x[0])
			if y > 0: y -= 2 * pi
			return y
		a = reversed(sorted(a, key=ang))
		c = 0
		for _, g in groupby(a, ang):
			c += 1
			if c == 200:
				g = list(sorted(g, key=lambda x : x[0].imag ** 2 + x[0].real ** 2))
				print(g[0][1][1] * 100 + g[0][1][0])
				exit()
