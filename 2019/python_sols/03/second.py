O = open('input').readlines()
a = O[0].split(",")
b = O[1].split(",")
v = []
for y in [a, b]:
	o = [0, 0]
	edg = []
	dict = {}
	dict[(0, 0)] = 0
	for x in y:
		d = x[0]
		z = int(x[1:])
		if d == 'D': u = [o[0] - z, o[1]]
		if d == 'U': u = [o[0] + z, o[1]]
		if d == 'L': u = [o[0], o[1] - z]
		if d == 'R': u = [o[0], o[1] + z]
		dict[(u[0], u[1])] = dict[(o[0], o[1])] + z
		edg.append([o, u])
		o = u
	k = []
	for (a, b) in edg:
		if a[1] > b[1] or a[0] > b[0]:
			k.append([b, a])
		else:
			k.append([a, b])
	v.append([k, dict])
r = 10 ** 10
for line1 in v[0][0]:
	for line2 in v[1][0]:
		A = line1
		B = line2
		C = v[0][1]
		D = v[1][1]
		if A[1][0] - A[0][0] == 0: A, B, C, D = B, A, D, C
		if A[1][0] - A[0][0] == 0: continue
		# A[1][0] - A[0][0] != 0
		if B[1][1] - B[0][1] == 0: continue
		if B[1][0] - B[0][0] != 0: continue
		assert A[1][0] - A[0][0] > 0
		assert B[1][1] - B[0][1] > 0
		if A[0][0] <= B[0][0] and B[0][0] <= A[1][0]:
			if B[0][1] <= A[0][1] and A[0][1] <= B[1][1]:
				assert (A[0][0], A[0][1]) in C
				assert (B[0][0], B[0][1]) in D
				if A[0] == [0, 0] or B[0] == [0,0]: continue
				aend = C[(A[0][0], A[0][1])] + (B[0][0] - A[0][0])
				astart = C[(A[1][0], A[1][1])] + (A[1][0] - B[0][0])
				adist = min(aend, astart)			
				bend = D[(B[0][0], B[0][1])] + (A[0][1] - B[0][1])
				bstart = D[(B[1][0], B[1][1])] + (B[1][1] - A[0][1])
				bdist = min(bend, bstart)			
				r = min(r, adist + bdist)
print(r)
