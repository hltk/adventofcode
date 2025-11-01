from math import gcd
g = []
for line in open("input").readlines():
	line = line.strip()
	g.append(list(line))
r = 0
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
		r = max(r, len(angls))
print(r)
