a = input().split(",")
b = input().split(",")
v = []
for y in [a, b]:
	o = [0, 0]
	edg = []
	for x in y:
		d = x[0]
		z = int(x[1:])
		if d == 'D': u = [o[0] - z, o[1]]
		if d == 'U': u = [o[0] + z, o[1]]
		if d == 'L': u = [o[0], o[1] - z]
		if d == 'R': u = [o[0], o[1] + z]
		edg.append([o, u])
		o = u
	k = []
	for (a, b) in edg:
		if a[1] > b[1] or a[0] > b[0]:
			k.append([b, a])
		else:
			k.append([a, b])
	v.append(k)
r = 10 ** 10
for line1 in v[0]:
	for line2 in v[1]:
		A = line1
		B = line2
		if A[1][0] - A[0][0] == 0: A, B = B, A
		if A[1][0] - A[0][0] == 0: continue
		# A[1][0] - A[0][0] != 0
		if B[1][1] - B[0][1] == 0: continue
		if B[1][0] - B[0][0] != 0: continue
		assert A[1][0] - A[0][0] != 0
		assert B[1][1] - B[0][1] != 0
		assert A[1][0] - A[0][0] > 0
		assert B[1][1] - B[0][1] > 0
		if A[0][0] <= B[0][0] and B[0][0] <= A[1][0]:
			if B[0][1] <= A[0][1] and A[0][1] <= B[1][1]:
				r = min(r, abs(B[0][0]) + abs(A[0][1]))
print(r)
