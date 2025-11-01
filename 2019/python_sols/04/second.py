def ok(x):
	u = str(x)
	ok = 1
	b = 0
	for j in range(1, len(u)):
		if u[j] < u[j - 1]: ok = 0
	return ok and any(u.count(a) == 2 for a in u)
a, b = map(int, open('input').readlines()[0].strip().split('-'))
print(sum(ok(x) for x in range(a, b + 1)))
