from collections import defaultdict
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
N = 6
M = 25
img = open("input").readlines()[0].strip()
dc = defaultdict(int)
for k in range(0, len(img), N * M):
	for y in range(0, N):
		for x in range(0, M):
			i = y * M + x
			u = int(img[k + i])
			if (y, x) not in dc.keys() and u != 2:
				dc[(y, x)] = u
printgridfromddict(dc)
