def ok(x):
	u = str(x)
	ok = 1
	b = 0
	for j in range(1, len(u)):
		if u[j] < u[j - 1]: ok = 0
		if u[j] == u[j - 1]: b = 1
	return ok and b
a, b = map(int, open('input').readlines()[0].strip().split('-'))
print(sum(ok(x) for x in range(a, b + 1)))
