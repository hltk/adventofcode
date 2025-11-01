from collections import defaultdict
cur = [('L', 10), ('L', 8), ('R', 8), ('L', 8), ('R', 6), ('L', 10), ('L', 8), ('R', 8), ('L', 8), ('R', 6), ('R', 6), ('R', 8), ('R', 8), ('R', 6), ('R', 6), ('L', 8), ('L', 10), ('R', 6), ('R', 8), ('R', 8), ('R', 6), ('R', 6), ('L', 8), ('L', 10), ('R', 6), ('R', 8), ('R', 8), ('R', 6), ('R', 6), ('L', 8), ('L', 10), ('R', 6), ('R', 8), ('R', 8), ('L', 10), ('L', 8), ('R', 8), ('L', 8), ('R', 6)]
occ = defaultdict(int)
for i in range(len(cur)):
	for j in range(i, len(cur)):
		occ[repr(cur[i : j + 1])] += 1
def split(cur, k, rep):
	K = []
	i = 0
	while i < len(cur):
		if len(cur) - i >= len(k) and cur[i:i+len(k)] == k:
			K.append(rep)
			i += len(k)
		else:
			K.append(cur[i])
			i += 1
	return K
def rep_best(cur, lvl, pro):
	if lvl == 3:
		ok = 1
		for u in cur:
			if u != None:
				ok = 0
		if not ok:
			return
		print("\n".join(pro))
		print()
	occ = defaultdict(int)
	for i in range(len(cur)):
		for j in range(i, len(cur)):
			substr = cur[i : j + 1]
			if None in substr:
				continue
			occ[repr(substr)] += 1
	best = 0
	best_it = None
	best_rep = None
	for k, v in sorted(occ.items(), key=lambda item: item[1], reverse=True):
		if v <= 1: continue
		if len(eval(k)) > 7: continue
		u = 0
		g = split(cur, eval(k), None)
		rep_best(g, lvl + 1, pro + [k])
rep_best(cur, 0, [])
exit()
# process answer
"""


def split(cur, k, rep):
	K = []
	A = []
	i = 0
	while i < len(cur):
		if len(cur) - i >= len(k) and cur[i:i+len(k)] == k:
			if A:K.append(A)
			A = []
			K.append(rep)
			i += len(k)
		else:
			A.append(cur[i])
			i += 1
	if A: K.append(A)
	return K
reps = [None] * 3
k = cur[: 5]
reps[0] = k
cur = split(cur, k, ord("A"))
ma = []
for i in range(len(cur)):
	if cur[i] != ord( "A"):
		assert reps[1] == None or reps[1] == cur[i][:3]
		reps[1] = cur[i][:3]
		ma.extend(split(cur[i], cur[i][:3], ord("B")))
	else: ma.append(cur[i])
ka = []
for i in range(len(ma)):
	if ma[i] != ord("A") and ma[i] != ord("B"):
		assert reps[2] == None or reps[2] == ma[i][:4]
		reps[2] = ma[i][:4]
		ka.extend(split(ma[i], ma[i][:4], ord("C")))
	else: ka.append(ma[i])
print(list(chr(x) for x in ka))
print(",".join(str(x) for x in ka) + ",10")
print()
for b in reps:
	y = []
	for a in b:
		y.append(a[0])
		y.append(a[1])
	print(y)
	print(len(y))
	x = ""
	for a in y:
		for p in str(a):
			x += p
	#print(x,len(x))
	x += "\n"
	print(",".join(str(ord(y)) for y in x))
"""
