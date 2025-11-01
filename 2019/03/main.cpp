a = input().split(",")
b = input().split(",")
def calc(P):
	d = {}
	o = [0, 0]
	steps = 0
	for x in P:
		D = x[0]
		z = int(x[1:])
		for _ in range(z):
			if D == 'D': o[0] -= 1
			if D == 'U': o[0] += 1
			if D == 'L': o[1] -= 1
			if D == 'R': o[1] += 1
			pa = (o[0], o[1])
			if not pa in d: d[pa] = steps
			steps += 1
	return d
A,B = calc(a), calc(b)
P = set(A.keys()) & set(B.keys())
# 1st subtask
mi = min([abs(p[0])+abs(p[1])for p in P])
print(mi)
# 2nd subtask
mi = min([A[p] + B[p] for p in P])
print(mi)
